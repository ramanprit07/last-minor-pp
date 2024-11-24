import mysql.connector
connection=None

try:
    connection= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        db='user_database'
    )
    if connection.is_connected():
        return connection
except mysql.connector.Error as e:
    print(f"Error: {e}")
    return None
    

cursor= connection.cursor(buffered=True)


def addUser(data):
    try:
        cursor.execute('INSERT into `users` (`username`,`password`) Values (%s,%s)',data)
        connection.commit()
        return True
    except Exception as e:
        print(f"Error is {e}")
        return False
    
def getAllUser():
    try:
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
    
def updateUser(data):
    try:
        cursor.execute('UPDATE `users` SET username=%s,  password=%s Where id=%s',data )
        connection.commit()
        return True
    except Exception as e:
        print("Error ",e)
        return False

def login(username, password):
    try:
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except Exception as e:
        print("Error is",e)
        return False
