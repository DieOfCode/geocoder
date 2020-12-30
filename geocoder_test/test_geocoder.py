from unittest.mock import patch

from pytest import fixture

from geo.geo_answer import GeoAnswer
from geo.geocoder import Geocoder
from geo.repository import GeoDatabase
from geocoder_test.test_data_base import TestDatabase


@fixture
def test_geocoder() -> Geocoder:
    return Geocoder(raw_address="Бердяжки улица Тургенева 4",
                    database=GeoDatabase())


@patch('geo.geocoder.GeoDatabase.database_connect',
       return_value=TestDatabase())
@patch('geo.geocoder.GeoDatabase.select_region', return_value=(1, "Ямайка"))
@patch('geo.geocoder.GeoDatabase.get_coordinate',
       return_value=(56.841067, 60.614769))
def test_success_geocode(test_database, test_region, test_coordinate,
                         test_geocoder: Geocoder):
    assert test_geocoder.find_geo_data() == GeoAnswer('Ямайка', 'Бердяжки',
                                                      'Тургенева',
                                                      'улица Тургенева 4',
                                                      56.841067,
                                                      60.614769)
