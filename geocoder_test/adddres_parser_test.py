from unittest.mock import patch

from pytest import fixture

from geo.address_parser import AddressParser
from geo.repository import GeoDatabase


@fixture
def test_address_parser() -> AddressParser:
    return AddressParser()


@patch("geo.address_parser.GeoDatabase.is_valid_city", return_value=True)
def test_city_and_street_without_dash(test_valid_city,
                                      test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4",GeoDatabase()).city == 'ЙошкарОла'


@patch("geo.address_parser.GeoDatabase.is_valid_city", return_value=True)
def test_street_with_literal(test_valid_city,
                             test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4",GeoDatabase()).street == 'Тургенева'
