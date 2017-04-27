from sqlalchemy import Column, Integer, String
from sermonapp.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


def Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)