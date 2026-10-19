
from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user="root",
        password=os.getenv("DB_PASSWORD", "rootpraktikum123"),
        database=os.getenv("DB_NAME", "simple_app")
    )

@app.route("/")
def home():
    return "Halo dari Flask + Docker + Jenkins!"

@app.route("/db")
def check_database():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return f"Koneksi MySQL berhasil! Database: {result[0]}"
    except Exception as e:
        return f"Koneksi MySQL gagal: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
