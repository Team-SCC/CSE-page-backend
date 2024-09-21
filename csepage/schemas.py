from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    sid: int
    name: str
    grade: int
    birth: date
    email: str
    auth: int


class StudentCreate(StudentBase):
    gender: str | None = None
    phone: str | None = None
    nickname: str | None = None


class Student(StudentBase):
    gender: str | None = None
    phone: str | None = None
    nickname: str | None = None
    password: str

    class Config:
        from_attributes = True  # orm_mode : pydantic V1. now V2


class SessionBase(BaseModel):
    uuid: int
    sid: int

    class Config:
        from_attributes = True  # orm_mode : pydantic V1. now V2


class LockerReservationBase(BaseModel):
    studentNumber: int
    lockerNumber: int
    date: date
    used: bool

    class Config:
        from_attributes = True  # orm_mode : pydantic V1. now V2
