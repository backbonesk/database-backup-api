from . import crud
from .database import db


def scheduler_job():
    schedules = crud.get_db_schedules(db)
    for schedule in schedules:
        print(schedule.__dict__)
