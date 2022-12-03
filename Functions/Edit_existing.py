def editUser(id,username,surname,email,mobile,password,address,dob):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update Normal_user set  username=? ,email=?,  passwd = ? ,surname=?, address = ?,mobile=?,dob=? where user_id = ? ;"
    cursor1.execute(query1,(username,email,password,surname,address,mobile,dob,id))
    connection.commit()

def editAdmin(id,username,surname,password):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update Admin_user set username=? , surname=? , passwd = ? where admin_id = ? ;"
    cursor1.execute(query1,(username,surname,password,id))
    connection.commit()
def editStock(id,name,symbol,cur_price,cur_date):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "update Stock set stock_name=? , stock_symbol=? , cur_price = ? ,cur_date=? where stock_id = ? ;"#curdate()???
    cursor1.execute(query1,(name,symbol,cur_price,cur_date,id))
    connection.commit()



def createConnection():
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection