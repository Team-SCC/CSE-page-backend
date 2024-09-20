from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Enum,
    ForeignKeyConstraint,
    CheckConstraint,
)

from csepage.enum import AuthEnum
from csepage.database import Base
from csepage.utils import default_end_date


class Student(Base):
    __tablename__ = "students"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sid = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    birth = Column(DateTime, nullable=False)
    password = Column(String, nullable=False)
    auth = Column(Enum(AuthEnum), nullable=False, default=AuthEnum.NORMAL)


class Session(Base):
    __tablename__ = "sessions"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String, nullable=False, index=True)
    sid = Column(String, nullable=False)


class FreeBoard(Base):
    __tablename__ = "freeboard"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sid = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    comment_count = Column(Integer, nullable=False, default=0)
    create_date = Column(DateTime, nullable=False)
    modified_date = Column(DateTime, nullable=True)


class Comment(Base):
    __tablename__ = "comments"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    freeboard_id = Column(Integer, nullable=False, index=True)
    sid = Column(String, nullable=False, index=True)
    content = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)

    __table_args__ = (ForeignKeyConstraint(["freeboard_id", ["freeboard._id"]]),)


class NoticeBoard(Base):
    __tablename__ = "noticeboard"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    create_date = Column(DateTime, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    end_date = Column(DateTime, nullable=True, default=default_end_date)


class Locker(Base):
    __tablename__ = "locker"

    _id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, nullable=False, index=True)
    sid = Column(Integer, nullable=False)
    use_date = Column(DateTime, nullable=False)
    is_use = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        CheckConstraint("number >= 1 AND number <= 50", name="check_number_range"),
    )
