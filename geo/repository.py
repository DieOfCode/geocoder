import psycopg2

from config import base
from geo.database_exception import DatabaseException
from geo.geo_exception import UnknownRegion, UnknownCity, UnknownStreet, \
    NoInfoInDatabase


class GeoDatabase:

    @staticmethod
    def database_connect():
        try:
            connection = psycopg2.connect(database=base.DATABASE,
                                          user=base.USER,
                                          host=base.HOST,
                                          port=base.DATABASE_PORT)
        except Exception:
            raise DatabaseException()

        return connection

    def is_valid_city(self, city) -> bool:
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute("select exists (select 1 from cities where city=%s)",
                        (city,))
            return cur.fetchone()[0]

    def is_valid_street(self, street):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select exists (select 1 "
                "from streets where position(%s in street)>0)",
                (street,))
            return cur.fetchone()[0]

    def is_valid_home(self, house) -> bool:
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select exists (select 1 from buildings where house=%s)",
                (house,))
            return cur.fetchone()[0]

    def select_region(self, city):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute("select regions.region_id,region "
                        "from regions inner join region_city "
                        "on region_city.region_id = regions.region_id "
                        "inner join cities "
                        "on cities.city_id = region_city.city_id "
                        "where city = %s", (city,))
            region_data = cur.fetchone()
            if region_data is None:
                raise UnknownRegion()
            return region_data

    def select_city_id(self, city):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute("select city_id from cities where city=%s", (city,))
            city_id = cur.fetchone()[0]
            if city_id is None:
                raise UnknownCity()
            return city_id

    def select_street_id(self, city_id, street):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select streets.street_id "
                "from streets inner join city_street "
                "on city_street.street_id = streets.street_id "
                "where city_id = %s and position(%s in street)>0",
                (city_id, street))
            street_id = cur.fetchone()[0]
            if street_id is None:
                raise UnknownStreet()
            return street_id

    def select_building_id(self, street_id=None, building=None):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select buildings.building_id from buildings "
                "inner join street_building "
                "on street_building.building_id = buildings.building_id "
                "where street_id = %s and house =%s",
                [street_id, building])
            building_id = cur.fetchone()[0]
            if building_id is None:
                raise NoInfoInDatabase()

            return building_id

    def get_coordinate(self, region_id, city_id, street_id, building_id):
        with self.database_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select lat,lon from geocode where region_id = %s "
                "and city_id = %s and street_id = %s and building_id = %s",
                (region_id, city_id, street_id, building_id))
            coordinates = cur.fetchone()
            if coordinates is None:
                raise NoInfoInDatabase()
            return coordinates