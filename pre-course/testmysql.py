class Config:
  MYSQL_HOST = 'db4free.net'
  MYSQL_PORT = 3306  # default port ของ MySQL คือ 3306
  MYSQL_USER = 'datath'
  MYSQL_PASSWORD = 'DataScience-chillchill'
  MYSQL_DB = 'detraining'
  MYSQL_CHARSET = 'utf8mb4'

import pymysql.cursors
import pandas as pd

# Connect to the database
connection = pymysql.connect(host=Config.MYSQL_HOST,
                             port=Config.MYSQL_PORT,
                             user=Config.MYSQL_USER,
                             password=Config.MYSQL_PASSWORD,
                             db=Config.MYSQL_DB,
                             cursorclass=pymysql.cursors.DictCursor)

# list all tables
cursor = connection.cursor()
cursor.execute("show tables;")
tables = cursor.fetchall()
cursor.close()
# print(tables)

# Use with statement instead of cursor.close()
with connection.cursor() as cursor:
  # Read a single record
  sql = "SELECT * FROM online_retail limit 500;"
  cursor.execute(sql)
  result = cursor.fetchall()

print(result)
