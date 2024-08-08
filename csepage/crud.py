from sqlalchemy.orm import Session

import models, schemas

def get_student(db: Session, student_sid: int):
    return db.query(models.Student).filter(models.Student.sid == student_sid).first()

def get_name(db: Session, grade: int):
    return db.query(models.Student).filter(models.Student.grade == grade).first()

def create_student(db: Session, student: schemas.StudentCreate) -> None:
    default_password = student.birth.strftime('%y%m%d') # default password set password = Birth(YYMMDD)

    new_student = models.Student(
        sid = student.sid,
        name = student.name,
        gender = student.gender,
        grade = student.grade,
        phone = student.phone,
        birth = student.birth,
        email = student.email,
        password = default_password,
        nickname = student.nickname,
        auth = student.auth
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def create_session(db: Session, session: schemas.SessionBase) -> None:
    new_session = models.Session(
        uuid = session.uuid,
        sid = session.sid
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

def create_lockerreservation(db: Session, session: schemas.LockerReservationBase) -> None:
    new_reservation = models.LockerReservation(
        studentNumber = session.studentNumber,
        lockerNumber = session.lockerNumber,
        date = session.date,
        used = session.used
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)