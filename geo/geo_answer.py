from dataclasses import dataclass


@dataclass
class GeoAnswer:
    region: str
    city: str
    street: str
    building_number: str
    building_literal:str
    latitude: float
    longitude: float
    country: str = "РОССИЯ"

    def __str__(self) -> str:
        return f"""
        Координаты:{self.latitude},{self.longitude}
        Страна:Россия
        Регион:{self.region}
        Населённый Пункт:{self.city}
        Улица:{self.street}
        Дом:{self.building_number}{self.building_literal 
        if self.building_literal else ""} 
        """
