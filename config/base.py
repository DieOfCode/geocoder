import os

DATABASE = "geo"
HOST = "127.0.0.1"
DATABASE_PORT = "5432"
USER = "postgres"
PASSWORD = os.environ.get('password')

HTTP_PORT = 8080
