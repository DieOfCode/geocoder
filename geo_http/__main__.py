from config import base
from geo_http.app import app

if __name__ == "__main__":
    app.run(host=base.HOST, port=base.HTTP_PORT, debug=True)
