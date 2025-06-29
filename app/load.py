import psycopg2
import pyodbc
import logging
import json
from config import *

def connect_pg():
    return psycopg2.connect(
        dbname=PG_DB, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT
    )

def connect_mssql():
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={MSSQL_HOST},{MSSQL_PORT};"
        f"DATABASE=master;"
        f"UID={MSSQL_USER};"
        f"PWD={MSSQL_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

def clean_value(key, value):
    if key == "company" and isinstance(value, dict):
        return value.get("name")
    if value is None:
        return None
    elif isinstance(value, (dict, list)):
        return json.dumps(value)
    else:
        return str(value)

def load_to_pg(table_name, data, cursor, clear_first=True):
    if clear_first:
        cursor.execute(f"DELETE FROM {table_name};")
    for item in data:
        cleaned_item = {k: clean_value(k, v) for k, v in item.items()}
        columns = ', '.join(cleaned_item.keys())
        placeholders = ', '.join(['%s'] * len(cleaned_item))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
        cursor.execute(sql, list(cleaned_item.values()))
    logging.info(f"Loaded {len(data)} rows into {table_name}")

def load_to_mssql(table_name, data, cursor):
    for item in data:
        cleaned_item = {k: clean_value(k, v) for k, v in item.items()}
        columns = ', '.join(cleaned_item.keys())
        placeholders = ', '.join(['?'] * len(cleaned_item))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
        cursor.execute(sql, list(cleaned_item.values()))
    logging.info(f"Loaded {len(data)} rows into {table_name}")
