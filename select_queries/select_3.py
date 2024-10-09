from connection import connect_to_database
from sqlalchemy import func, desc
from models import Student, Grade, Group


def select_3():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Group.name,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .where(Grade.subject_id == 22)
        .group_by(Group.id)
        .order_by(desc('avg_grade'))
        .all()
    )

    for group, avg_grade in results:
        print(f'Group - {group}, average grade - {avg_grade}')
