from unittest.mock import patch

from pytest import fixture

from geo.address_parser import AddressParser


@fixture
def test_address_parser() -> AddressParser:
    return AddressParser()


@patch("geo.address_parser.AddressParser.is_valid_city", return_value=True)
def test_address_with_dash(test_valid_city,
                           test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address("Йошкар-Ола Тургенева 4") == (
        "Йошкар-Ола", "Тургенева", 4)


@patch("geo.address_parser.AddressParser.is_valid_city", return_value=True)
def test_street_with_dash(test_valid_city, test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address("Йошкар Турге-нева 4") == (
        "Йошкар", "Турге-нева", 4)


@patch("geo.address_parser.AddressParser.is_valid_city", return_value=True)
def test_city_and_street_with_dash(test_valid_city,
                                   test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address(
        "Йошкар-Ола Турге-нева 4") == ("Йошкар-Ола", "Турге-нева", 4)


@patch("geo.address_parser.AddressParser.is_valid_city", return_value=True)
def test_city_and_street_without_dash(test_valid_city,
                                      test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4") == (
           "ЙошкарОла", "Тургенева лучшая улица", 4)


@patch("geo.address_parser.AddressParser.is_valid_city", return_value=True)
def test_street_with_literal(test_valid_city,
                             test_address_parser: AddressParser):
    assert test_address_parser.get_parse_address(
        "ЙошкарОла Тургенева лучшая улица 4") == ("ЙошкарОла", "Тургенева "
                                                               "лучшая "
                                                               "улица", 4)
