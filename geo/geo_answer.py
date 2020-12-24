from dataclasses import dataclass


@dataclass
class GeoAnswer:
    region: str
    city: str
    street: str
    building_number: int
    building_literal: str = None
    latitude: float = None
    longitude: float = None
    country: str = "РОССИЯ"

    def __str__(self) -> str:
        return f"Координаты:{self.latitude},{self.longitude}\nСтрана:Россия\n" \
               f"Регион:{self.region}\nНаселённый Пункт:{self.city}\n" \
               f"Улица:{self.street}\nДом:{self.building_number}" \
               f"{self.building_literal if self.building_literal else ''}"
