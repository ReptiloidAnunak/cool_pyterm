import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from settings import DB_ABSPATH, DB_SQLITE_PATH


if not os.path.exists(os.path.dirname(DB_ABSPATH)):
    os.makedirs(os.path.dirname(DB_ABSPATH))


engine = create_engine(DB_SQLITE_PATH)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def create_db_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    init_db()
    session = create_db_session()
