from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Enum,
)

from csepage.enum import AuthEnum
from csepage.database import Base
from csepage.utils import default_end_date


class Student(Base):
    __tablename__ = "students"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sid = Column(String(8), nullable=False, index=True)
    name = Column(String(16), nullable=False, index=True)
    birth = Column(DateTime, nullable=False)
    password = Column(String(255), nullable=False)
    auth = Column(Enum(AuthEnum), nullable=False, default=AuthEnum.NORMAL)


class Session(Base):
    __tablename__ = "sessions"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String(255), nullable=False, index=True)
    sid = Column(String(8), nullable=False)


class FreeBoard(Base):
    __tablename__ = "freeboard"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sid = Column(String(8), nullable=False, index=True)
    title = Column(String(32), nullable=False)
    content = Column(String(1024), nullable=False)
    comment_count = Column(Integer, nullable=False, default=0)
    create_date = Column(DateTime, nullable=False)
    modified_date = Column(DateTime, nullable=True)


class Comment(Base):
    __tablename__ = "comments"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    freeboard_id = Column(Integer, nullable=False, index=True)
    sid = Column(String(8), nullable=False, index=True)
    content = Column(String(1024), nullable=False)
    create_date = Column(DateTime, nullable=False)


class NoticeBoard(Base):
    __tablename__ = "noticeboard"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(16), nullable=False, index=True)
    create_date = Column(DateTime, nullable=False)
    title = Column(String(32), nullable=False)
    content = Column(String(1024), nullable=False)
    end_date = Column(DateTime, nullable=True, default=default_end_date)


class Locker(Base):
    __tablename__ = "locker"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, nullable=False, index=True)
    sid = Column(Integer, nullable=False)
    use_date = Column(DateTime, nullable=False)
    is_use = Column(Boolean, nullable=False, default=True)
