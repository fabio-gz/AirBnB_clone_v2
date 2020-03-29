#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), ablenull=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """returns the list of City instances with
        state_id equals to the current State.id
        """
        my_list = []
        for key, value in models.storage.all(City).items():
            if value.states_id == self.id:
                my_list.append(value)
        return my_list
