from pytest import fixture

from geo.geo_answer import GeoAnswer


@fixture
def test_geo_answer() -> GeoAnswer:
    return GeoAnswer(region="Свердловская область", city="Екатеринбург",
                     street="Тургенева", building="4",
                     latitude=56.34543, longitude=60.234234)


def test_answer(test_geo_answer):
    assert str(test_geo_answer) == "Координаты:56.34543," \
                                   "60.234234\nСтрана:Россия\n" \
                                   "Регион:Свердловская область\nНаселённый " \
                                   "Пункт:Екатеринбург\n" \
                                   "Улица:Тургенева\nДом:4\n"
