#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = Relationship('Place', secondary=place_amenity)
