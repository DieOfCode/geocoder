import logging
from dataclasses import dataclass

from geo.geo_exception import UnknownCity, UnknownAddress, \
    NoGeocoderDataException
from geo.geocoder import Geocoder

logging.basicConfig(filename="geo.log", filemode="w",
                    format='%(name)s - %(levelname)s - %(message)s')


@dataclass
class CLI:
    _status: str = "start"
    raw_data: str = ""
    working: bool = True

    def get_answer(self) -> str:
        while True:

            if self._status == "start":
                print("Введи адресс, получи более интересную информацию \n"
                      "Формат ввода адресса: Город Улица Номер дома\n"
                      "Чтобы прекратить работу введите конец или \\end \n"
                      "Для получения краткой информации введите \\help \n")
                self.raw_data = input()
                if self.raw_data.lower() == "\\end":
                    break
                if self.raw_data.lower() == "\\help":
                    print("Простое приложение для получения гео данных "
                          "объекта\n"
                          "Для получения необходимой информации введите\n"
                          "Данные об объекте в фромате Город Улица Номер "
                          "дома \n")
                    self._status= "start"
                self._status = "wait_answer"
            if self._status == "wait_answer":
                if self.raw_data == "":
                    print(
                        "Ну, ты подумай, не торопись. "
                        "И введи адрес. Не надо нам тут баловаться")
                    self._status = "start"

                try:
                    geocoder = Geocoder(self.raw_data)
                    yield geocoder.find_geo_data()
                    self._status = "start"
                except NoGeocoderDataException as geocoder_data_exception:
                    geocoder_data_exception.exception_handling(
                        self.raw_data)
                except UnknownCity as city_exception:
                    city_exception.exception_handling(self.raw_data)
                except UnknownAddress as address_exception:
                    address_exception.exception_handling(self.raw_data)
                except Exception as another_exception:
                    print("Что-то пошло совсем не так")
                    logging.exception("address:{} ,{} {}"
                                      .format(self.raw_data, "АЛЯРМ!!!!!",
                                              another_exception.__str__()))
                finally:
                    self._status = "start"
