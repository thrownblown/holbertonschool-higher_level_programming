#!/usr/bin/python3
"""makin states alchemiclly"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
