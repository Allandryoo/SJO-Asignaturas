from flask import Flask
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres123@localhost:5432/mydb')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.route('/')
def hello():
    return "Flask con PostgreSQL funcionando"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)