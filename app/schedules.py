import logging
import subprocess
import threading
from . import crud
from .database import db
from .models import Backup, BackupStatus

from dateutil.rrule import rrulestr
from datetime import datetime


def create_backup(schedule: Backup):
    crud.update_backup_schedule_status(db, str(schedule.id), BackupStatus.running)
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
                "{}.bak".format(schedule.destination),
                str(schedule.dbname),
            ]
        )
        if int(process.returncode) != 0:
            raise

        crud.update_backup_schedule_status(db, str(schedule.id), BackupStatus.finished)
    except Exception as e:
        logging.error(f"Backup error: {e}")
        crud.update_backup_schedule_status(db, str(schedule.id), BackupStatus.failed)


def scheduler_job():
    now = datetime.now()
    now = now.replace(second=0, microsecond=0)
    schedules = crud.get_backup_schedules(db)

    for schedule in schedules:
        if schedule.status == BackupStatus.running:  # type: ignore
            continue
        rule = rrulestr(schedule.rrulestring)
        dt = list(rule)[0]
        if dt > now:
            t = threading.Thread(target=create_backup, args=(schedule,))
            t.start()
