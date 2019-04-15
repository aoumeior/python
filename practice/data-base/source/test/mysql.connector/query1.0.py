import datetime
import mysql.connector

config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'chat',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT email, nickname, birthday FROM user_info "
         "WHERE birthday BETWEEN %s AND %s")

bir_start = datetime.date(2019, 1, 1)
bir_end = datetime.date(2019, 3, 1)

cursor.execute(query, (bir_start, bir_end))

for (email, nickname, birthday) in cursor:
    print("{}, {} birthday is {:%d %b %Y}".format(
        email, nickname, birthday))

cursor.close()
cnx.close()
