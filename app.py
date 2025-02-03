from flask import Flask
import mysql.connector

app_instance = Flask(__name__)

@app_instance.route("/")
def home():
    return "Hello! This is a Flask app running inside a Docker container. Deploy anywhere with ease!"

@app_instance.route("/mysql")
def database_status():
    try:
        db_connection = mysql.connector.connect(
            host="mysql-container",  
            user="root",
            password="admin",
            database="mysql"
        )
        if db_connection.is_connected():
            return "Successfully connected to MySQL database!"
    except Exception as error:
        return str(error)

if __name__ == "__main__":
    app_instance.run(host="0.0.0.0", port=5000)
