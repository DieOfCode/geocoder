import functools
import logging

from flask import Flask, request

from geo.geo_exception import GeoException
from geo.geocoder import Geocoder
from geo.repository import GeoDatabase
from geo_http import geo_http_exception

app = Flask(__package__)

logger = logging.getLogger(__name__)

DATABASE = GeoDatabase()


def json_api(func):
    @functools.wraps(func)
    def wrapper():
        try:
            return func()
        except geo_http_exception.GeoAPIException as e:
            return e.message, e.http_code
        except GeoException as e:
            return e.message, 400
        except Exception as e:
            logger.exception(f"{type(e)}: {e}")
            return "unhandled server error", 500

    return wrapper


@app.route("/get_geocode", methods=['POST'])
@json_api
def get_geocode():
    raw_geo_data = request.get_data()
    geocoder = Geocoder(raw_geo_data.decode("utf-8"), DATABASE)
    return str(geocoder.find_geo_data())
