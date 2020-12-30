from dataclasses import dataclass

from geo.address_parser import AddressParser
from geo.geo_answer import GeoAnswer
from geo.repository import GeoDatabase


@dataclass
class Geocoder:
    raw_address: str
    database: GeoDatabase

    def find_geo_data(self) -> GeoAnswer:
        address_parser = AddressParser()
        parse_address = address_parser.get_parse_address(self.raw_address,
                                                         self.database)
        region_id, region = self.database.select_region(parse_address.city)
        city_id = self.database.select_city_id(parse_address.city)
        street_id = self.database.select_street_id(city_id,
                                                   address_parser.street)
        building_id = self.database.select_building_id(street_id,
                                                       parse_address.house)
        coordinate = self.database.get_coordinate(region_id, city_id,
                                                  street_id, building_id)
        return GeoAnswer(region=region, city=parse_address.city,
                         street=parse_address.street,
                         building=parse_address.house,
                         latitude=float(coordinate[0]),
                         longitude=float(coordinate[1]))
