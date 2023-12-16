#!/usr/bin/python3
"""Defines a link class for city objects for the cities database table
"""

from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City link class to cities table"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    states = relationship("State", back_populates="cities")
