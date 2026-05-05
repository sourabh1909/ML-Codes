import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1', # 127.0.1.1
        port = 3300,
        user = 'root',
        password ='sourabh'
    )
    mycursor = conn.cursor()
    print('connection establish')
except:
    print('connection error')
    
# //this command run only single time
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table 
# airport -> airport_id | code | name |city
# mycursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
mycursor.execute("USE indigo")

# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
#                  """)

# conn.commit()


# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','New Dehli','IGIA'),                
# (2,'CCU','Kolkata','NSCA'),   
# (3,'BOM','Mumbai','CSMA')   
#                  """)

# conn.commit()

mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
# data = mycursor.fetchone()  # for one
data = mycursor.fetchall() #for one or more
print(data)

for i in data:
    print(i[3])
    
    
# update
# mycursor.execute("""
#         UPDATE airport
#         SET city = 'Bombay'
#         WHERE airport_id = 3
#                  """)
# conn.commit()

# mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
# data = mycursor.fetchall() #for one or more
# print(data)

# mycursor.execute("""
#         DROP TABLE airport
#                  """)
# conn.commit()

mycursor.execute("""
        SELECT * FROM airport
                 """)
data = mycursor.fetchall()

for i in data:
    print(i)