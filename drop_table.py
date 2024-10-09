from sqlalchemy import create_engine
from models import Base

def drop_table():
    engine = create_engine('postgresql+psycopg2://dima:qseft135@localhost:5432/sqlalchemy')

    Base.metadata.drop_all(engine)

