import sqlalchemy
from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_backup_schedules(db: Session):
    return db.query(models.BackupSchedules).all()


def get_backup_schedules_public(db: Session):
    results = db.query(
        models.BackupSchedules.database_name,
        models.BackupSchedules.host,
        models.BackupSchedules.rrule_string,
    ).all()
    result_dicts = []
    for result in results:
        result_dicts.append(
            {
                "database_name": result.database_name,
                "host": result.host,
                "rrule_string": result.rrule_string,
            }
        )
    return result_dicts
