import logging

logging.basicConfig(filename="geo.log", filemode="w",
                    format='%(name)s - %(levelname)s - %(message)s')


class GeoException(Exception):
    message: str

    def exception_handling(self, raw_address) -> None:
        print(self.message)


class UnknownCity(GeoException):
    message = "Неизвестный нам город"


class UnknownAddress(GeoException):
    message = "Проверьте правильность адреса"


class NoGeocoderDataException(GeoException):
    message = "Мы не знаем где это,здесь водятся драконы"


class MissingGeoInformation(GeoException):
    message = "Отсутствуют необхоимые аргументы"


class UnknownRegion(GeoException):
    message = "Неизвестный район"


class UnknownStreet(GeoException):
    message = "Неизвестный улица"


class UnknownBuilding(GeoException):
    message = "Неизвестный номер дома"


class NoInfoInDatabase(GeoException):
    message = "Информции по данному объекту нет"
