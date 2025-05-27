import os
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "usuario"),
        password=os.getenv("DB_PASSWORD", "usuariopassword"),
        database=os.getenv("DB_NAME", "mensajes")
    )

@app.route("/")
def hola_mundo():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT mensaje FROM mensajes WHERE id = 1")
        row = cursor.fetchone()
        if row:
            return jsonify({"mensaje": row[0]})
        else:
            return jsonify({"mensaje": "No message found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
