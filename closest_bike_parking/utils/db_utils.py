import csv
import logging

import sqlalchemy
from sqlalchemy.exc import IntegrityError

from closest_bike_parking.db.core import engine, session
from closest_bike_parking.db.models import BikeStation


def is_data_loaded() -> bool:
    return sqlalchemy.inspect(engine).has_table(BikeStation.__tablename__)


def load_csv(csv_filename: str):
    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            row = {
                'free': True if row['gratuit'] == 'true' else False,
                'x': float(row['X']),
                'y': float(row['Y']),
                'id': row['id_local']
            }
            session.add(
                BikeStation(**row)
            )
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
                logging.info(str(e))
