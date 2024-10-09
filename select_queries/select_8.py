from connection import connect_to_database
from sqlalchemy import func
from models import Grade, Subject, Teacher


def select_8():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            func.avg(Grade.grade).label('avg_grade'),
            Teacher.name,
            Subject.name
        )
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .where(Teacher.id == 27)
        .group_by(Teacher.name, Subject.name)
        .all()
    )

    for grade, teacher, subject in results:
        print(f'Teacher - {teacher}, subject - {subject}, grade - {grade}')
