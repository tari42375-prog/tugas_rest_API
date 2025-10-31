# from app import app

from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': "",
    'database': 'flaskmysql'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'Username': row[1],
            'Password': row[2],
            'Email': row[3],
            'Alamat': row[4],
            'NoTelepon': row[5]
        })
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)