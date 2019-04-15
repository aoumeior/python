#! /bin/usr/python3

import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='chat')

'''

<mysql.connector.connection.MySQLConnection object at 0x7f0625671438 >

'''

print(cnx)
cnx.close()
