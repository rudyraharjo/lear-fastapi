from sqlalchemy.orm import Session
from app.utils.database import db_engine


def get_db_session():
    session = Session(db_engine)
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()