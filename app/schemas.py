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


class BackupSchedules(BaseModel):
    host: str
    port: int
    dbname: str
    username: str
    password: str
    rrulestring: str

    class Config:
        orm_mode = True


@dataclass
class BackupSchedulesForm:
    host: str = Form(...)
    port: int = Form(...)
    dbname: str = Form(...)
    username: str = Form(...)
    password: str = Form(...)
    rrulestring: str = Form(...)
