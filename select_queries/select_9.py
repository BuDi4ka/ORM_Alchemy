from connection import connect_to_database
from sqlalchemy import distinct
from models import Student, Grade, Subject


def select_9():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            distinct(Subject.name),
            Student.name
        )
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .where(Student.id == 178)
        .group_by(Student.name, Subject.name)
        .limit(5)
        .all()
    )

    for subject, student in results:
        print(f'Subject - {subject}, student - {student}')
