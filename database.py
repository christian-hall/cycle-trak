import mysql.connector

def connect_to_database():
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
            return True

    except mysql.connector.Error as e:
        print('Error while connecting to MySQL', e)
        return False


def query_database(query, object):
    pass

