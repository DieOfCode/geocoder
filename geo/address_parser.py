import dataclasses

from geo.geo_exception import NoGeocoderDataException
from geo.repository import GeoDatabase


@dataclasses.dataclass()
class AddressParser:
    street: str = ""
    city: str = ""
    house: str = ""

    @classmethod
    def get_parse_address(cls, raw_address: str, database: GeoDatabase):
        address_fragment = raw_address.strip(" ").split(" ")
        for i in range(len(address_fragment)):
            raw_city = " ".join(address_fragment[:i])
            if database.is_valid_city(raw_city) and raw_city != '':
                cls.city = raw_city
                address_fragment = address_fragment[i:]
                i += 1
                break
        for i in range(len(address_fragment)):
            raw_street = " ".join(address_fragment[:i])
            if database.is_valid_street(raw_street) and raw_street != '':
                if not database.is_valid_street(
                        " ".join(address_fragment[:i + 1])):
                    cls.street = raw_street
                    address_fragment = address_fragment[i:]
                    break
        cls.house = " ".join(address_fragment)
        if cls.house == "" or cls.house == "":
            raise NoGeocoderDataException
        return cls
