#!/usr/bin/python3
"""
defines the states database table link class
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """states table link class."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(128), nullable=False)
