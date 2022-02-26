
# python dbconfig.py

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector import connect

dbconfig = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "website"
}


cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=20,
    pool_reset_session=True,
    autocommit=True,
    **dbconfig
)
