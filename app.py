import logging
import os
import sqlite3

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY is not configured.")

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/users")
def search_users(username: str = Query(..., min_length=1, max_length=50)):
    try:
        conn = sqlite3.connect("users.db")

        query = """
            SELECT id, username, email
            FROM users
            WHERE username = ?
        """

        rows = conn.execute(query, (username,)).fetchall()

        return {
            "users": [
                {
                    "id": row[0],
                    "username": row[1],
                    "email": row[2],
                }
                for row in rows
            ]
        }

    except sqlite3.Error:
        logger.exception("Database error while searching users")
        raise HTTPException(
            status_code=500,
            detail="Unable to process the request.",
        )

    finally:
        if "conn" in locals():
            conn.close()
