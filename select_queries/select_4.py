from connection import connect_to_database
from sqlalchemy import func, desc
from models import Grade


def select_4():
    session = connect_to_database()
    db = session()
    results = (
        db.query(
            func.avg(Grade.grade).label('avg_grade')
        ).scalar()
    )

    print(f'Avarage grade - {results}')
