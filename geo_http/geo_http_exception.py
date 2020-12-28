class GeoAPIException(Exception):
    http_code = 500
    message: str


class InvalidContent(GeoAPIException):
    http_code = 400
    message = "text body expected"


class MissingData(GeoAPIException):
    http_code = 400
    message = "missing data"
