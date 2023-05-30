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
    id: int
    host: str
    port: int
    database_name: str
    username: str
    password: str
    rrule_string: str

    class Config:
        orm_mode = True
