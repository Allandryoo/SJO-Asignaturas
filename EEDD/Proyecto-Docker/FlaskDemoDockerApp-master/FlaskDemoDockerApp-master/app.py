from flask import Flask
from mysql import connector 
import random,dotenv,os

dotenv.load_dotenv() # Carga las variables de entorno desde el archivo .env

app = Flask(__name__)

def init_mySQL():
    try:
        connection = connector.connect(
            host=os.getenv("DATABASE_HOST"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            port=os.getenv("DATABASE_PORT")
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection    
    except connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

def exec_query(query, params=None):
    connection = init_mySQL()
    if connection:
        cursor = connection.cursor(buffered=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor
        except connector.Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()
            connection.close()

def config_mySQL():
    QUERY='''CREATE TABLE IF NOT EXISTS Customer (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )'''
    exec_query(QUERY)

@app.route("/")
def index():
    config_mySQL()
    return "Welcome to this demo app!"

@app.route("/customers")
def get_customers():
    QUERY = "SELECT id, name FROM Customer"
    cursor = exec_query(QUERY)
    customers = cursor.fetchall()
    return "<br>".join([f"ID: {id}, Name: {name}" for id, name in customers])


@app.route("/insert")
def insert_into_ddb():
    QUERY="INSERT INTO Customer (name) VALUES (%s)"
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    name = names[random.randint(0, len(names)-1)]
    exec_query(QUERY, (name,))
    return f"Inserted customer: {name}"
    