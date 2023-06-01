from sqlalchemy.orm import Session

from . import schemas
from .models import BackupStatus, User, Backup


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_backup_schedules(db: Session):
    return db.query(Backup).all()


def get_backup_schedules_public(db: Session):
    results = db.query(
        Backup.id,
        Backup.dbname,
        Backup.host,
        Backup.rrulestring,
        Backup.status,
    ).all()
    result_dicts = []
    for result in results:
        result_dicts.append(
            {
                "uuid": result.id,
                "dbname": result.dbname,
                "host": result.host,
                "rrulestring": result.rrulestring,
                "status": result.status,
            }
        )
    return result_dicts


def create_backup_schedule(db: Session, form_data: schemas.Backup):
    row = Backup(**form_data.dict(), status=BackupStatus.scheduled)
    db.add(row)
    db.commit()
    db.refresh(row)


def delete_backup_schedule(db: Session, uuid: str):
    db.query(Backup).filter(Backup.id == uuid).delete()
    db.commit()


def update_backup_schedule_status(db: Session, uuid: str, status: BackupStatus):
    schedule = db.query(Backup).filter(Backup.id == uuid)
    schedule.update({Backup.status: status})
    db.commit()
