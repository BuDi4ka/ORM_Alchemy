from connection import connect_to_database
from sqlalchemy import func, desc
from models import Student, Grade


def select_1():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        )
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(desc('average_grade'))
        .limit(5)
        .all()
    )

    for student, avg_grade in results:
        print(f"Student: {student}, Average Grade: {avg_grade}")