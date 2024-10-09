from connection import connect_to_database
from models import Subject, Teacher


def select_5():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Subject.name,
        )
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .where(Teacher.id == 27)
        .all()
    )

    for teacher in results:
        print(f'All subjects - {teacher}')

