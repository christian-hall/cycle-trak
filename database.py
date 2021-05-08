import mysql.connector

try:
    connection = mysql.connector.connect(user='ct_user',
                                        password='sesame',
                                        host='localhost',
                                        database='cycletrak',
                                        auth_plugin='mysql_native_password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except mysql.connector.Error as e:
    print('Error while connecting to MySQL', e)


def connected():
    if connection.is_connected():
        return True
    else:
        return False

def query_one(query):
    query = cursor.execture(query)
    results = cursor.fetchall()

def query_many(query):
    pass

def query_all(query):
    pass