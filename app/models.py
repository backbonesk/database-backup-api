import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String)
    password = Column(String)


class BackupStatus(enum.Enum):
    scheduled = "scheduled"
    running = "running"
    finished = "finished"
    failed = "failed"


class Backup(Base):
    __tablename__ = "backups"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    host = Column(String)
    port = Column(Integer)
    dbname = Column(String)
    username = Column(String(100))
    password = Column(String(100))
    rrule = Column(String)
    destination = Column(String)
    status = Column(Enum(BackupStatus))


class BackupRecord(Base):
    __tablename__ = "backup_records"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(Enum(BackupStatus))
    destination = Column(String)
    created_at = Column(DateTime, default=datetime.now)
