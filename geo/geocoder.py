from dataclasses import dataclass

import psycopg2

from geo.address_parser import AddressParser
from geo.geo_answer import GeoAnswer
from geo.geo_exception import NoGeocoderDataException


@dataclass
class Geocoder():
    database: str = "test_geocoder_data"
    user: str = "postgres"
    host: str = "localhost"
    port: str = "5432"

    def data_base_connect(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                host=self.host,
                                port=self.port)

    def find_geo_data(self, raw_address: str) -> GeoAnswer:
        address_parser = AddressParser()
        parse_address = address_parser.get_parse_address(raw_address)
        with self.data_base_connect() as connection:
            cur = connection.cursor()
            cur.execute(
                "select region,city,street,house,lat,lon "
                "from cities inner join geocode "
                "on cities.city_id = geocode.city_id "
                "inner join regions on geocode.region_id = regions.region_id "
                "inner join streets on geocode.street_id = streets.street_id "
                "inner join buildings "
                "on geocode.building_id = buildings.building_id "
                "where city = %s "
                "and position(%s in street)>0 and buildings.house = %s",
                parse_address)
            data = cur.fetchall()
            if not data:
                raise NoGeocoderDataException()
            return GeoAnswer(region=data[0][0], city=data[0][1],
                             street=data[0][2], building=data[0][3],
                             latitude=float(data[0][4]),
                             longitude=float(data[0][5]))
