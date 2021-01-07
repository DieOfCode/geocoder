from unittest.mock import patch

from psycopg2._psycopg import cursor
from pytest import fixture

from geo.address_parser import AddressParser
from geo.repository import GeoDatabase
from geocoder_test.test_data_base import TestDatabase, TestCursor


@fixture
def test_address_parser() -> AddressParser:
    return AddressParser()


@fixture
def test_cursor() -> TestCursor:
    test_database = TestDatabase()
    return test_database.cursor()


@patch("geo.address_parser.GeoDatabase.is_valid_city", return_value=True)
def test_city_and_street_without_dash(test_valid_city,
                                      test_address_parser: AddressParser, test_cursor: TestCursor):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4", GeoDatabase(test_cursor)).city == 'ЙошкарОла'


@patch("geo.address_parser.GeoDatabase.is_valid_city", return_value=True)
def test_street_with_literal(test_valid_city,
                             test_address_parser: AddressParser,test_cursor: TestCursor):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4", GeoDatabase(test_cursor)).city == 'ЙошкарОла'
