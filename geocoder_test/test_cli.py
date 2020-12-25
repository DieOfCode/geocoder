from unittest.mock import patch

from pytest import fixture

from geo.CLI import CLI
from geo.geo_answer import GeoAnswer


@fixture
def test_cli() -> CLI:
    return CLI()


@patch('builtins.input', return_value="Бердяжки улица Тургенева 4")
def test_get_answer(test_input, test_cli: CLI):
    for answer in test_cli.get_answer():
        assert answer == GeoAnswer(region='Ямайка',
                                   city='Бердяжки',
                                   street='улица Тургенева',
                                   building="4",
                                   latitude=56.841067,
                                   longitude=60.614769)
        break
