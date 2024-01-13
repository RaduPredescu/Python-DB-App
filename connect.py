import mysql.connector
from utils import Config, read_params

params = read_params('config.yaml')
config = Config(params=params)


def connect_to_database():
    username = config.client.username
    password = config.client.password
    database_name = config.client.database_name
    host = config.client.host

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host=host, user=username, password=password, database=database_name
    )

    return connection
