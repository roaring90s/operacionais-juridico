import os
import psycopg2 as pg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return pg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )