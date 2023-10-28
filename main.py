from __future__ import annotations

import os
import sqlite3
from sqlite3 import Connection
import more_itertools

from fastapi import FastAPI


DB_DIR = 'db'
DB_FILE = f'{DB_DIR}/database.db'


def get_connection(db_file: str) -> Connection:
    try:
        # TODO: check_same_thread sounds risky
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except sqlite3.OperationalError:
        return initialize_db(db_file)
    else:
        return conn


def initialize_db(db_file: str) -> Connection:
    os.makedirs(DB_DIR, exist_ok=True)
    open(db_file, 'w+').close()

    # TODO: check_same_thread sounds risky
    conn = sqlite3.connect(db_file, check_same_thread=False)

    with open('schema/schema.sql') as file:
        conn.executescript(file.read())
    with open('backup/data.sql') as file:
        # for idx, piece in enumerate(read_in_chunks(file)):
        for idx, chunk in enumerate(more_itertools.chunked(file.readlines(), 1024)):
            print(f'chunk {idx}')
            conn.executescript("\n".join(chunk))
    return conn


def read_in_chunks(file, chunk: int = 1024):
    while True:
        data = file.read(chunk)
        if not data:
            break
        yield data


app = FastAPI()
CONN = get_connection(DB_FILE)


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/count')
def get_count() -> dict[str, int]:
    with CONN as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) from items')
        count = int(cursor.fetchone()[0])
        return {'count': count}

@app.get('/get')
def get_count(name) -> object:
    with CONN as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT title, cat, dt FROM items WHERE title LIKE ? LIMIT 100', (like_str(name),))
        return {'result': cursor.fetchall()}

def like_str(text: str) -> str:
    return '%' + text + '%'
