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
    return db.query(models.BackupSchedule).all()


def get_backup_schedules_public(db: Session):
    results = db.query(
        models.BackupSchedule.id,
        models.BackupSchedule.dbname,
        models.BackupSchedule.host,
        models.BackupSchedule.rrulestring,
    ).all()
    result_dicts = []
    for result in results:
        result_dicts.append(
            {
                "uuid": result.id,
                "dbname": result.dbname,
                "host": result.host,
                "rrulestring": result.rrulestring,
            }
        )
    return result_dicts


def create_backup_schedule(db: Session, form_data: schemas.BackupScheduleForm):
    # TODO: Refactor
    row = models.BackupSchedule(
        host=form_data.host,
        port=form_data.port,
        dbname=form_data.dbname,
        username=form_data.username,
        password=form_data.password,
        rrulestring=form_data.rrulestring,
        backupdest=form_data.backupdest,
    )
    db.add(row)
    db.commit()
    db.refresh(row)


def delete_backup_schedule(db: Session, uuid: str):
    db.query(models.BackupSchedule).filter(models.BackupSchedule.id == uuid).delete()
    db.commit()
