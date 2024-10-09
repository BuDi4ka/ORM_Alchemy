import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')

if not all([DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("One or more environment variables are missing!")

DATABASE_URL = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from models import Base
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

