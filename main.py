import datetime
from collections.abc import Generator
from contextlib import contextmanager

from alembic import command
from alembic.config import Config
from sqlalchemy import Engine
from sqlmodel import Session, create_engine, text

from models import User


def create_connection() -> Engine:
    db_engine: Engine = create_engine("sqlite:///database.sqlite")

    with db_engine.connect() as conn:
        # unused in this example but kept in case it matters for the issue
        conn.execute(text("PRAGMA foreign_keys=ON"))

    return db_engine


@contextmanager
def get_session() -> Generator[Session]:
    session = Session(create_connection(), expire_on_commit=False)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_user():
    with get_session() as session:
        user = User(
            email_address="test@example.com",
            created_at=int(datetime.now().timestamp()),
            external_id="1234567890",
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"User created with ID {user.id}")


def db_migrations():
    command.upgrade(Config("alembic.ini"), "head")


if __name__ == "__main__":
    db_migrations()
    create_user()
