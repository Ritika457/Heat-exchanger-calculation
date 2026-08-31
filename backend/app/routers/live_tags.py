from fastapi import APIRouter
from app.database.connection import get_connection

router = APIRouter()


@router.get("/live-tags")
def get_live_tags():

    conn = get_connection()
    cursor = conn.cursor()

    # SQL query yahan aayegi
    cursor.execute("""
        SELECT Name, Value, Time
        FROM Heat_Exchanger_Taglist
        WHERE Time = (
            SELECT MAX(Time)
            FROM Heat_Exchanger_Taglist
        )
        ORDER BY Name
    """)
    columns = [column[0] for column in cursor.description]

    data = []

    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))

    conn.close()

    return data