from sqlalchemy.orm import Mapped, mapped_column
from . import Base
from sqlalchemy import String
from sqlalchemy import select

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(32), unique = True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"

def select_users(session):
    stmt = select(User).where(User.name.in_(['michaelis', 'bob']))
    for user in session.scalars(stmt):
        print(user)