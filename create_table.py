from connection import connect_to_database
from models import Base  # Імпортуємо Base, щоб мати доступ до моделей

def create_tables():
    SessionLocal, engine = connect_to_database()  # Отримуємо сесію та engine
    try:
        # Створюємо всі таблиці в базі даних
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error occurred while creating tables: {e}")
    finally:
        SessionLocal().close()  # Закриваємо сесію

if __name__ == "__main__":
    create_tables()
