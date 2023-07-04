from sqlalchemy import Column, Boolean, Float, String

from closest_bike_parking.db.core import Model


class BikeStation(Model):
    __tablename__ = 'bike_stations'

    id = Column('id', String, primary_key=True)
    x = Column('x', Float)
    y = Column('y', Float)
    free = Column('free', Boolean)
