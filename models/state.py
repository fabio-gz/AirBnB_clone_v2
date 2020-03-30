#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes: name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances with
        state_id equals to the current State.id
        """
        objects = models.storage.all()
        my_list = []
        res = []
        for key in objects:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                my_list.append(objects[key])
        for i in my_list:
            if i.state_id == self.id:
                res.append(i)

        return res
