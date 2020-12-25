from pytest import fixture

from geo.geo_answer import GeoAnswer
from geo.geocoder import Geocoder


@fixture
def test_geocoder() -> Geocoder:
    return Geocoder(database='test_geocoder_data', user="postgres",
                    password="Vanish878", host='localhost', port="5432")


def test_success_geocode(test_geocoder: Geocoder):
    assert test_geocoder.find_geo_data(
        "Бердяжки улица Тургенева 4") == GeoAnswer(region='Ямайка',
                                                   city='Бердяжки',
                                                   street='улица Тургенева',
                                                   building="4",
                                                   latitude=56.841067,
                                                   longitude=60.614769)
