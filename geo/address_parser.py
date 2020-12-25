import dataclasses
from typing import Tuple

import psycopg2


@dataclasses.dataclass()
class AddressParser:
    street: str = ""
    city: str = ""
    house: str = -1
    city_and_street: str = None
    literal = None

    def get_parse_address(self, raw_address: str) -> Tuple[str, str, str]:
        address_fragment = raw_address.split(" ")
        for i in range(len(address_fragment)):
            raw_city = " ".join(address_fragment[:i])
            if self.is_valid_city(raw_city) and raw_city != '':
                self.city = raw_city
                address_fragment = address_fragment[i:]
                i += 1
                break
        for i in range(len(address_fragment)):
            raw_street = " ".join(address_fragment[:i])
            if self.is_valid_street(raw_street) and raw_street != '':
                if not self.is_valid_street(
                        " ".join(address_fragment[:i + 1])):
                    self.street = raw_street
                    address_fragment = address_fragment[i:]
                    break
        self.house = " ".join(address_fragment)
        if self.house == "" or self.street == "" or self.house == "":
            raise Exception
        return self.city, self.street, self.house

    def is_valid_city(self, city) -> bool:
        with psycopg2.connect(host="localhost", dbname="test_geocoder_data",
                              user="postgres") as connection:
            cur = connection.cursor()
            cur.execute("select exists (select 1 from cities where city=%s)",
                        (city,))
            return cur.fetchone()[0]

    def is_valid_street(self, street):
        with psycopg2.connect(host="localhost", dbname="test_geocoder_data",
                              user="postgres") as connection:
            cur = connection.cursor()
            cur.execute(
                "select exists (select 1 "
                "from streets where position(%s in street)>0)",
                (street,))
            return cur.fetchone()[0]

    def is_valid_home(self, house) -> bool:
        with psycopg2.connect(host="localhost", dbname="test_geocoder_data",
                              user="postgres") as connection:
            cur = connection.cursor()
            cur.execute(
                "select exists (select 1 from buildings where house=%s)",
                (house,))
            return cur.fetchone()[0]
