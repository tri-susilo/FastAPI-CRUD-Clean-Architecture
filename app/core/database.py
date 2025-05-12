from sqlmodel import SQLModel, create_engine
from app.core.config import settings
from contextlib import contextmanager
from sqlmodel import Session

engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
    from app.models import users
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session