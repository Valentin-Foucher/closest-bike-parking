import webbrowser

from closest_bike_parking import config
from closest_bike_parking.db.core import init_db
from closest_bike_parking.db.query import get_closest_station_coordinates
from closest_bike_parking.utils.db_utils import is_data_loaded, load_csv

data_loaded = is_data_loaded()

init_db()

if not data_loaded:
    load_csv(config.get('bicycle_station_file'))

coordinates = get_closest_station_coordinates(7.7647035, 48.5873799997946)
webbrowser.open(f'https://www.google.com/maps/search/?api=1&query={coordinates[1]}%2C{coordinates[0]}')
