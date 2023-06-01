import enum
import uuid
from sqlalchemy import Column, String, Integer, Enum
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
    username = Column(String)
    password = Column(String)
    rrulestring = Column(String)
    destination = Column(String)
    status = Column(Enum(BackupStatus))
