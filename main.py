from fastapi import FastAPI

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Entity.User import User, select_users
from Entity import Base, engine
from Api.User import *

app = FastAPI()


if (__name__ == "__main__"):
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        mika = User(name = 'michaelis')
        bob = User(name = 'bob')
        try:
            session.add_all([mika, bob])
            session.commit()
        except IntegrityError as e:
            session.rollback()
            print(type(e))
        
        select_users(session)
                