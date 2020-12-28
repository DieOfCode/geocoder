from decimal import Decimal
from unittest.mock import patch

from pytest import fixture

from geo.geo_answer import GeoAnswer
from geo.geocoder import Geocoder
from geocoder_test.test_data_base import TestDatabase


@fixture
def test_geocoder() -> Geocoder:
    return Geocoder(database='test_geocoder_data', user="postgres",
                    host='localhost', port="5432", raw_address="Бердяжки "
                                                               "улица "
                                                               "Тургенева 4")


@patch('geo.geocoder.Geocoder.data_base_connect', return_value=TestDatabase())
def test_success_geocode(test_database, test_geocoder: Geocoder):
    assert test_geocoder.find_geo_data() == GeoAnswer(('Ямайка', 'Бердяжки',
                                                       'улица Тургенева',
                                                       '4',
                                                       Decimal('56.841067'),
                                                       Decimal('60.614769')))
