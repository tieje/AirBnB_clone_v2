#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
=======
"""`City` class definition."""
from models.base_model import BaseModel
>>>>>>> a6c6b079ece7aba29f3feb7cdc436c5bc67b6c48
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


<<<<<<< HEAD
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
=======
class City(BaseModel):
    """The city in which a place is located."""
>>>>>>> a6c6b079ece7aba29f3feb7cdc436c5bc67b6c48
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship('State')
    places = relationship("Place", backref="cities", cascade="all")
