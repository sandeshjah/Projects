from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL DB connection config
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "NEW12345"
}

@app.route("/data", methods=["GET"])

def get_data():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Example query
        cursor.execute("SELECt emp,ename FROM EMP;")
        rows = cursor.fetchall()

        # Format data as list of dictionaries
        result = [{"id": row[0], "name": row[1]} for row in rows]

        # Clean up
        cursor.close()
        conn.close()

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)
