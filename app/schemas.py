from dataclasses import dataclass
from fastapi import Form
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class BackupSchedule(BaseModel):
    host: str
    port: int
    dbname: str
    username: str
    password: str
    rrulestring: str
    backupdest: str

    class Config:
        orm_mode = True
