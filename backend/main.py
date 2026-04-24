from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "luhn")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASSWORD", "admin")


def luhn(number):
    digits = [int(x) for x in str(number)][::-1]
    total = 0

    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return total % 10 == 0


def save(number):
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO valid_numbers(number) VALUES (%s)", (number,))
    conn.commit()
    cur.close()
    conn.close()


@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    number = data.get("number")

    if not number:
        return jsonify({"valid": False, "message": "Número vacío"}), 400

    if luhn(number):
        try:
            save(number)
        except Exception as e:
            return jsonify({"valid": True, "message": "Válido pero error en BD"}), 500

        return jsonify({"valid": True, "message": "Número válido"})
    else:
        return jsonify({"valid": False, "message": "Número inválido"})


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)