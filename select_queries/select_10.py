from connection import connect_to_database
from sqlalchemy import and_
from models import Student, Grade, Subject, Teacher


def select_10():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Subject.name,
            Teacher.name,
            Student.name
        )
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .where(
            and_(
                Teacher.id == 27,
                Student.id == 178
            )
        )
        .all()
    )

    for subject, teacher, student in results:
        print(f'Subject - {subject}, teacher - {teacher}, student - {student}')
