import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root", 
    password="123123", 
    database="personal_finance"
)

cursor = conn.cursor()



# cursor.execute("SELECT * from transactions")
# for row in cursor:
#     print(row)

# conn.commit()
# conn.close()

# print("Connection sucessfully done")
