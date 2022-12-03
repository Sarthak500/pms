import mysql.connector
def createConnection():
    
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection


def userlogin(username, password):
    connection = createConnection()
    query = "select passwd,user_id from Normal_user where username = '{}';".format(username)
    cursor1 = connection.cursor()
    # cursor1.execute(query,(id))
    cursor1.execute(query)
    value = cursor1.fetchall()
    #print("debug1 ****************** " + str(value))
    if len(value) > 0:
        #print("debug2 ****************** " + str(value))
        if password == value[0][0]:
            return value[0][1]
        else:
            return 0
    else:
        return 0


def adminlogin(username, password):
    connection = createConnection()
    query = "select passwd,admin_id from Admin_user where username = '{}';".format(username)
    cursor1 = connection.cursor()
    cursor1.execute(query)
    value = cursor1.fetchall()
    if len(value) > 0:
        if password == value[0][0]:
            return value[0][1]
        else:
            return 0
    else:
        return 0
