from sqlalchemy import text

from closest_bike_parking.db.core import session
from closest_bike_parking.db.models import BikeStation


def get_closest_station_coordinates(x: float, y: float) -> (float, float):
    result = session.execute(text('SELECT x, y, SQRT(POWER(x - :x, 2) + POWER(y - :y, 2)) AS distance\n'
                                  f'FROM {BikeStation.__tablename__}\n'
                                  'WHERE free IS true\n'
                                  'ORDER BY distance ASC\n'
                                  'LIMIT 1'), {'x': x, 'y': y}).first()
    return result[0], result[1]
