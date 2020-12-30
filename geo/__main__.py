import logging

from geo.database_exception import DatabaseException
from geo.geo_exception import GeoException
from geo.geocoder import Geocoder
from geo.repository import GeoDatabase

logging.basicConfig(filename="geo.log", filemode="w",
                    format='%(name)s - %(levelname)s - %(message)s')




def main():
    _status: str = "start"
    raw_data = ""
    cursor = GeoDatabase.database_connect()
    while True:

        if _status == "start":
            print("Введи адресс, получи более интересную информацию \n"
                  "Формат ввода адресса: Город Улица Номер дома\n"
                  "Чтобы прекратить работу введите конец или \\end \n"
                  "Для получения краткой информации введите \\help \n")
            raw_data = input()
            if raw_data.lower() == "\\end":
                break
            if raw_data.lower() == "\\help":
                print("Простое приложение для получения гео данных "
                      "объекта\n"
                      "Для получения необходимой информации введите\n"
                      "Данные об объекте в фромате Город Улица Номер "
                      "дома \n")
                _status = "start"
            _status = "wait_answer"
        if _status == "wait_answer":
            if raw_data == "":
                print(
                    "Ну, ты подумай, не торопись. "
                    "И введи адрес. Не надо нам тут баловаться")
                _status = "start"

            try:
                geocoder = Geocoder(raw_data, cursor)
                yield geocoder.find_geo_data()
                _status = "start"
            except GeoException as geocoder_data_exception:
                print(geocoder_data_exception.message)

                logging.exception(
                    "address:{} ,{}".format(raw_data,
                                            geocoder_data_exception.message), )
                exit(1)
            except DatabaseException as exception:
                print(exception.message)
                logging.exception(
                    "address:{} ,{}".format(raw_data,
                                            exception.message), )
                exit(1)
            except Exception as another_exception:
                print("Что-то пошло совсем не так")
                logging.exception("address:{} ,{} {}"
                                  .format(raw_data, "АЛЯРМ!!!!!",
                                          another_exception.__str__()))
                exit(1)
            finally:
                _status = "start"


if __name__ == '__main__':
    for geocode in main():
        print(geocode)
