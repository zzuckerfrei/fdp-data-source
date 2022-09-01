from typing import Generator
from db import session

# from db.session import SessionLocal
# from db.session import Client


def get_db() -> Generator:
    try:
        # db = SessionLocal()
        db = session.SessionLocal()
        yield db
    finally:
        db.close()


def get_client():
    print("111111")
    return session.get_client()
