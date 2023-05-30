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
        models.BackupSchedules.dbname,
        models.BackupSchedules.host,
        models.BackupSchedules.rrulestring,
    ).all()
    result_dicts = []
    for result in results:
        result_dicts.append(
            {
                "dbname": result.dbname,
                "host": result.host,
                "rrulestring": result.rrulestring,
            }
        )
    return result_dicts


def create_backup_schedule(db: Session, form_data: schemas.BackupSchedulesForm):
    # TODO: Refactor
    row = models.BackupSchedules(
        host=form_data.host,
        port=form_data.port,
        dbname=form_data.dbname,
        username=form_data.username,
        password=form_data.password,
        rrulestring=form_data.rrulestring,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
