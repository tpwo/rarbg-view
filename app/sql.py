from __future__ import annotations

import logging
import os
import sqlite3
from sqlite3 import Connection

QUERY_FTS5 = """\
CREATE VIRTUAL TABLE IF NOT EXISTS items_fts USING fts5(
    title,
    content='items',
    content_rowid='rowid'
)
"""

# Check if FTS5 table is empty
#
# This is a bit stupid, but this table is non-empty after the query
# above creates items_fts. But we still have to fill it with data.
#
# So we check for sample match `abc` which should return something.
# DB state is quite static in this project, so this is good enough for now.
QUERY_FTS5_CHECK = """\
SELECT COUNT(*) FROM items_fts
JOIN items i on i.rowid = items_fts.rowid
WHERE items_fts MATCH "abc"
"""

QUERY_FTS5_INSERT = """\
INSERT INTO items_fts(rowid, title)
SELECT rowid, title FROM items
"""


def ensure_fts5_table(connection: Connection) -> None:
    """Ensures FTS5 table exists and is populated if empty."""
    cursor = connection.cursor()
    logging.info("Ensuring FTS5 table 'items_fts' exists...")
    cursor.execute(QUERY_FTS5)
    logging.info("FTS5 table 'items_fts' checked/created.")
    cursor.execute(QUERY_FTS5_CHECK)
    count = cursor.fetchone()[0]
    if count == 0:
        logging.info("FTS5 table 'items_fts' is empty. Populating from 'items' table...")
        cursor.execute(QUERY_FTS5_INSERT)
        logging.info("FTS5 table 'items_fts' population complete.")
    else:
        logging.info("FTS5 table 'items_fts' already populated.")
    connection.commit()


def get_connection(db_file: str) -> Connection:
    if os.path.exists(db_file):
        # NOTE: `check_same_thread` is False, as DB is READ ONLY
        return sqlite3.connect(db_file, check_same_thread=False)
    else:
        raise SystemExit(
            f'ERROR: database file `{db_file}` not found. Please provide it and rerun the app.'
        )
