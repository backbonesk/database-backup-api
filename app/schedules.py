import subprocess
from . import crud
from .database import db
from .models import BackupSchedule

from dateutil.rrule import rrulestr
from datetime import datetime


def create_backup(schedule: BackupSchedule):
    try:
        subprocess.run(
            [
                "pg_dump",
                "-U",
                str(schedule.username),
                "-d",
                str(schedule.dbname),
                "-f",
                "{}.sql".format(schedule.backupdest),
            ]
        )
    except:
        pass


def scheduler_job():
    now = datetime.now()
    now = now.replace(second=0, microsecond=0)
    schedules = crud.get_backup_schedules(db)

    for schedule in schedules:
        rule = rrulestr(schedule.rrulestring)
        dt = list(rule)[0]
        min_diff = (dt - now).total_seconds() / 60
        if min_diff < 1:
            create_backup(schedule)
