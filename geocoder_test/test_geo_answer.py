from pytest import fixture

from geo.geo_answer import GeoAnswer


@fixture
def test_geo_answer() -> GeoAnswer:
    return GeoAnswer(region="Свердловская область", city="Екатеринбург",
                     street="Тургенева", building_number=4,
                     latitude=56.34543, longitude=60.234234)


def test_answer(test_geo_answer):
    assert str(test_geo_answer) == f"Координаты:56.34543,60.234234\nСтрана:Россия\n" \
               f"Регион:Свердловская область\nНаселённый Пункт:Екатеринбург\n" \
               f"Улица:Тургенева\nДом:4"
