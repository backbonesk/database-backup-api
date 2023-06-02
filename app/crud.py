from sqlalchemy.orm import Session

from . import schemas
from .models import BackupRecord, BackupStatus, User, Backup
from .config import settings


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_backup_schedules(db: Session):
    return db.query(Backup).all()


def get_backup_schedules_public(db: Session):
    results = db.query(
        Backup.id,
        Backup.dbname,
        Backup.host,
        Backup.rrule,
    ).all()
    result_dicts = []
    for result in results:
        result_dicts.append(
            {
                "uuid": result.id,
                "dbname": result.dbname,
                "host": result.host,
                "rrule": result.rrule,
            }
        )
    return result_dicts


def get_backup_schedule_records(db: Session, backup_id: str):
    return db.query(BackupRecord).filter(BackupRecord.backup_id == backup_id).all()


def create_backup_schedule(db: Session, form_data: schemas.Backup):
    backup_dict = {
        **form_data.dict(),
        "destination": "{}/{}".format(settings.BASE_DIR, form_data.destination),
    }
    row = Backup(**backup_dict)
    db.add(row)
    db.commit()
    db.refresh(row)


def delete_backup_schedule(db: Session, uuid: str):
    db.query(Backup).filter(Backup.id == uuid).delete()
    db.commit()


def create_backup_record(db: Session, record: BackupRecord):
    db.add(record)
    db.commit()
    db.refresh(record)
