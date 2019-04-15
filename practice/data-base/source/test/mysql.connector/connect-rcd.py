import mysql.connector
# https: // dev.mysql.com/doc/connector-python/en/connector-python-installation.html
config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'chat',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
