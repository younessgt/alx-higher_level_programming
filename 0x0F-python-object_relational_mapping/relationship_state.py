#!/usr/bin/python3
""" Python file that contains the class definition
of a State and an instance Base = declarative_base() """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """creating State class"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # cities is an instance of of SQLAlchemy's relationship class 
    # and behaves like a Python list
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
