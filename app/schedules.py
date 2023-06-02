import logging
import subprocess
import threading

from . import crud
from .database import db
from .models import Backup, BackupRecord, BackupStatus

from dateutil.rrule import rrulestr
from datetime import datetime


def create_backup(schedule: Backup):
    status = BackupStatus.running
    try:
        process = subprocess.run(
            [
                "pg_dump",
                "-h",
                str(schedule.host),
                "-p",
                str(schedule.port),
                "-U",
                str(schedule.username),
                "-f",
                str(schedule.destination),
                str(schedule.dbname),
            ]
        )
        if int(process.returncode) != 0:
            raise

        status = BackupStatus.finished
    except Exception as e:
        logging.error(f"Backup error: {e}")
        status = BackupStatus.failed
    crud.create_backup_record(
        db,
        BackupRecord(
            backup_id=schedule.id, status=status, destination=schedule.destination
        ),
    )


def scheduler_job():
    now = datetime.now()
    now = now.replace(second=0, microsecond=0)
    schedules = crud.get_backup_schedules(db)

    for schedule in schedules:
        rule = rrulestr(schedule.rrule)
        dt = list(rule)[0]
        minutes_diff = (dt - now).total_seconds() / 60
        if minutes_diff < 1:
            t = threading.Thread(target=create_backup, args=(schedule,))
            t.start()
