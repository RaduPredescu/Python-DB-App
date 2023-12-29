import mysql.connector


def connect_to_database():
    username = "root"
    password = "Mercedes22012002!"
    database_name = "proiect"

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost", user=username, password=password, database=database_name
    )

    return connection
