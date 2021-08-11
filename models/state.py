#!/usr/bin/python3
"""`State` class definition."""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """A US state."""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')

    @property
    def cities(self):
        """Return the list of `City` instances with `state_id`."""
        from models import storage
        citiesOState = []
        for c in storage.all(City).values():
            if c.state_id == self.id:
                citiesOState.append(c)
        return citiesOState
