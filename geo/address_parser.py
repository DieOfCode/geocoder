import dataclasses
import json
from collections import namedtuple
from typing import Tuple

import psycopg2

from geo.geo_exception import NoGeocoderDataException, UnknownCity

CITY = ['Бердяжки', ]


@dataclasses.dataclass()
class AddressParser:
    street: str = ""
    city: str = ""
    number: int = -1

    def get_parse_address(self, raw_address: str) -> Tuple[str, str, int]:
        city_and_street = raw_address.rsplit(" ", 1)[0]
        self.number = raw_address.rsplit(" ", 1)[1] if \
            raw_address.rsplit(" ", 1)[1].isnumeric() else 0
        if "-" in city_and_street:
            if city_and_street.find(" ") > city_and_street.find("-"):
                self.city = city_and_street.split(" ", 1)[0]
                self.street = city_and_street.split(" ", 1)[1]
            else:
                self.city, self.street = city_and_street.rsplit(" ", 1)
        else:
            data = city_and_street.split(" ")
            for i in range(len(data)):
                raw_city = " ".join(data[:i])
                city_and_street = data[1] if len(data) > 1 else None
                if raw_city != "" and self.is_valid_city(raw_city):
                    self.city = raw_city
                    self.street = " ".join(data[i:])
                    break
                if city_and_street is None:
                    raise UnknownCity()
        return self.city, self.street, int(self.number)

    def is_valid_city(self, city):
        with psycopg2.connect(host="localhost", dbname="test_geocoder_data",
                               user="postgres") as connection:
            cur = connection.cursor()
            cur.execute("select exists (select 1 from cities where city=%s)",
                        (city,))
            return cur.fetchone()
