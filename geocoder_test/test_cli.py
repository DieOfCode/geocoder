from decimal import Decimal
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
        assert answer == GeoAnswer(('Ямайка', 'Бердяжки', 'улица Тургенева',
                                    '4', Decimal('56.841067'),
                                    Decimal('60.614769')))
        break
