import subprocess
from . import crud
from .database import db
from .models import Backup, BackupStatus

from dateutil.rrule import rrulestr
from datetime import datetime


def create_backup(schedule: Backup):
    crud.update_backup_schedule_status(db, str(schedule.id), "running")
    try:
        process = subprocess.run(
            [
                "pg_dump",
                "-U",
                str(schedule.username),
                "-d",
                str(schedule.dbname),
                "-f",
                "{}.sql".format(schedule.dest),
            ]
        )
        if int(process.returncode) != 0:
            raise

        crud.update_backup_schedule_status(db, str(schedule.id), "finished")
    except:
        crud.update_backup_schedule_status(db, str(schedule.id), "failed")


def scheduler_job():
    now = datetime.now()
    now = now.replace(second=0, microsecond=0)
    schedules = crud.get_backup_schedules(db)

    for schedule in schedules:
        if schedule.status == BackupStatus.scheduled:  # type: ignore
            continue
        rule = rrulestr(schedule.rrulestring)
        dt = list(rule)[0]
        if dt > now:
            create_backup(schedule)
