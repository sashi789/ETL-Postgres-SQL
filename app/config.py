import os
from dotenv import load_dotenv

load_dotenv()


PG_USER = os.getenv("POSTGRES_USER")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD")
PG_DB = os.getenv("POSTGRES_DB")
PG_HOST = os.getenv("POSTGRES_HOST")
PG_PORT = os.getenv("POSTGRES_PORT")

MSSQL_USER = os.getenv("MSSQL_USER")
MSSQL_PASSWORD = os.getenv("MSSQL_PASSWORD")
MSSQL_DB = os.getenv("MSSQL_DB")
MSSQL_HOST = os.getenv("MSSQL_HOST")
MSSQL_PORT = os.getenv("MSSQL_PORT")

API_USERS_URL = os.getenv("API_USERS_URL")
API_POSTS_URL = os.getenv("API_POSTS_URL")
