from dataclasses import dataclass


@dataclass
class GeoAnswer:
    raw_geo_data: tuple

    def __post_init__(self):
        self.region: str = self.raw_geo_data[0]
        self.city: str = self.raw_geo_data[1]
        self.street: str = self.raw_geo_data[2]
        self.building: str = self.raw_geo_data[3]
        self.latitude: float = float(self.raw_geo_data[4])
        self.longitude: float = float(self.raw_geo_data[5])
        self.country: str = "РОССИЯ"

    def __str__(self) -> str:
        return f"Координаты:{self.latitude},{self.longitude}\nСтрана:Россия\n" \
               f"Регион:{self.region}\nНаселённый Пункт:{self.city}\n" \
               f"Улица:{self.street}\nДом:{self.building}\n"

# region=data[0][0], city=data[0][1],
#                              street=data[0][2], building=data[0][3],
#                              latitude=float(data[0][4]),
#                              longitude=float(data[0][5])
