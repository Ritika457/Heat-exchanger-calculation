from app.database.connection import get_connection

try:
    conn = get_connection()

    print("✅ Database Connected Successfully")

    cursor = conn.cursor()

    cursor.execute("SELECT DB_NAME()")

    db_name = cursor.fetchone()[0]

    print("Connected Database :", db_name)

    conn.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)