import os
from .Driver_sql import *
from dotenv import load_dotenv

load_dotenv(".env", override=True)

user = os.getenv("user_name_DB")
host = os.getenv("name_host_DB")
database = os.getenv("name_DB")
passw = os.getenv("password_DB")
port = os.getenv("port_DB")



def connection():
    connection = Driver_sql(database, host, user, passw, port)

    return connection
