from sqlalchemy import Column, String, Integer

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class BackupSchedules(Base):
    __tablename__ = "backup_schedules"
    id = Column(Integer, primary_key=True)
    host = Column(String)
    port = Column(Integer)
    database_name = Column(String)
    username = Column(String)
    password = Column(String)
    rrule_string = Column(String)
