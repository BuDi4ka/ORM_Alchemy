from connection import connect_to_database
from models import Student


def select_6():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            Student.name,
        )
        .where(Student.group_id == 17)
        .group_by(Student.name)
        .all()
    )

    for student in results:
        print(f'All students in certain group - {student}')
