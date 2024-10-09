from connection import connect_to_database
from sqlalchemy import func, desc
from models import Student, Grade


def select_2():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Student.name,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Grade, Student.id == Grade.student_id)
        .where(Grade.subject_id == 22)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(1)
        .all()
    )

    for student, avg_grade in results:
        print(f'Student - {student}, average grade - {avg_grade}')