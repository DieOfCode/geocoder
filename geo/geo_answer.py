from dataclasses import dataclass


@dataclass
class GeoAnswer:
    region: str
    city: str
    street: str
    building: str
    latitude: float
    longitude: float
    country: str = "РОССИЯ"

    def __str__(self) -> str:
        return f"Координаты:{self.latitude},{self.longitude}\nСтрана:Россия\n"\
               f"Регион:{self.region}\nНаселённый Пункт:{self.city}\n" \
               f"Улица:{self.street}\nДом:{self.building}\n"
