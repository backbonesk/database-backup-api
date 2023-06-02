import logging
import subprocess
import threading

from . import crud
from .database import db
from .models import Backup, BackupRecord, BackupStatus

from dateutil.rrule import rrulestr
from datetime import datetime


def create_backup(schedule: Backup):
    crud.update_backup_schedule_status(db, str(schedule.id), BackupStatus.running)
    status = BackupStatus.running
    try:
        crud.update_backup_schedule_status(db, str(schedule.id), status)
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
    crud.update_backup_schedule_status(db, str(schedule.id), status)
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
        if schedule.status == BackupStatus.running:  # type: ignore
            continue
        rule = rrulestr(schedule.rrule)
        dt = list(rule)[0]
        if dt < now:
            t = threading.Thread(target=create_backup, args=(schedule,))
            t.start()
