import mysql.connector
from utils import Config,read_params

params = read_params('config.yaml')
config = Config(params=params)


def connect_to_database():
    username = config.username
    password = config.password
    database_name = config.database_name
    host = config.host

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host=host, user=username, password=password, database=database_name
    )

    return connection
