from connection import connect_to_database
from sqlalchemy import and_
from models import Student, Grade, Group, Subject


def select_7():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Grade.grade,
            Subject.name.label('subject_name'),
            Group.name.label('group_name')
        )
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Group, Student.group_id == Group.id)
        .where(
            and_(
                Grade.subject_id == 22,
                Student.group_id == 17
            )
        )
        .all()
    )

    for grade, subject, group in results:
        print(f'Subject - {subject}, Group - {group}, Grade - {grade}')
