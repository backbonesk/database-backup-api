import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String)
    password = Column(String)


class BackupSchedules(Base):
    __tablename__ = "backup_schedules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    host = Column(String)
    port = Column(Integer)
    dbname = Column(String)
    username = Column(String)
    password = Column(String)
    rrulestring = Column(String)
