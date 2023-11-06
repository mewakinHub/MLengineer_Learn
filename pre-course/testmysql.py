# class Config:
#   MYSQL_HOST = 'db4free.net'
#   MYSQL_PORT = 3306  # default port ของ MySQL คือ 3306
#   MYSQL_USER = 'datath'
#   MYSQL_PASSWORD = 'DataScience-chillchill'
#   MYSQL_DB = 'detraining'
#   MYSQL_CHARSET = 'utf8mb4'

class Config:
  MYSQL_HOST = 'localhost'
  MYSQL_PORT = 3306  # default port ของ MySQL คือ 3306
  MYSQL_USER = 'root'
  MYSQL_PASSWORD = 'root'
  MYSQL_DB = 'employees'
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

# List all tables
# cursor = connection.cursor()
# cursor.execute("SHOW TABLES;")
# tables = cursor.fetchall()
# cursor.close()

# # Convert the result to a pandas DataFrame
# df = pd.DataFrame(tables, columns=['Tables_in_' + Config.MYSQL_DB])

# # Print the DataFrame
# print(df)

# Use with statement instead of cursor.close()
with connection.cursor() as cursor:
  # Read a single record
  sql = "SELECT * FROM employee_data limit 20;"
  cursor.execute(sql)
  result = cursor.fetchall()

# Convert the result to a pandas DataFrame
df = pd.DataFrame(result)

# Print the DataFrame
print(df)
