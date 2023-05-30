from . import crud
from .database import db


def scheduler_job():
    schedules = crud.get_backup_schedules(db)
    for schedule in schedules:
        pass
