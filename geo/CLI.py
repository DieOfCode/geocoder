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
    raw_address: str = ""
    working: bool = True

    def get_answer(self) -> str:
        while True:

            if self._status == "start":
                print("Введи адресс, получи более интересную информацию \n"
                      "Формат ввода адресса: Город Улица Номер дома\n"
                      "Чтобы прекратить работу введите конец или \\end \n""")
                self.raw_address = input()
                if self.raw_address.lower() == "\\end":
                    break
                self._status = "wait_answer"
            if self._status == "wait_answer":
                if self.raw_address == "":
                    print(
                        "Ну, ты подумай, не торопись. "
                        "И введи адрес. Не надо нам тут баловаться")
                    self._status = "start"

                try:
                    geocoder = Geocoder(self.raw_address)
                    yield geocoder.find_geo_data()
                    self._status = "start"
                except NoGeocoderDataException as geocoder_data_exception:
                    geocoder_data_exception.exception_handling(
                        self.raw_address)
                except UnknownCity as city_exception:
                    city_exception.exception_handling(self.raw_address)
                except UnknownAddress as address_exception:
                    address_exception.exception_handling(self.raw_address)
                except Exception as another_exception:
                    print("Что-то пошло совсем не так")
                    logging.exception("address:{} ,{} {}"
                                      .format(self.raw_address, "АЛЯРМ!!!!!",
                                              another_exception.__str__()))
                finally:
                    self._status = "start"
