import mysql.connector
def createConnection():
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection

def removeFromUser(user_id):#username??
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    string1 = "DELETE from Normal_user where user_id=?"
    cursor1.execute(string1,(user_id))
    string2 = "DELETE from Portfoliolisting where user_id=?"
    cursor1.execute(string2,(user_id))
    # string3 = "DELETE from doctor where doc_id=?;"
    # cursor1.execute(string3,(idx))
    connection.commit()
def removeFromStock(stock_id):#username??
    connection = createConnection()

    cursor1 = connection.cursor(prepared=True)

    query0="select cur_price from Stock where stock_id=? ;"
    cursor1.execute(query0,(stock_id))
    value = cursor1.fetchall()
    
    query3="select user_id,sum(quantity) from (select * from pms.Portfoliolisting where stock_id=?) as pls group by user_id,stock_id ;"
    cursor1.execute(query3,(stock_id))
    value = cursor1.fetchall()
    # diff=cur_price-cur_price_old
    for row in value:
        user_id=row[0]
        no=row[1]
        query4 = "update Normal_user set cash=cash+? where user_id = ? ;"
        cursor1.execute(query4,((value[0][0]*no),user_id))
        # connection.commit()
        # my_dict = {'f_name' : row[0],'user_id':row[1],'contact':row[2],'location':row[3], 'email':row[4]}
        # list1.append(my_dict)
    # return list1
    # connection.commit()
    string2 = "DELETE from Portfoliolisting where stock_id=? ;"
    cursor1.execute(string2,(stock_id))
    
    string1 = "DELETE from Stock where stock_id=? ;"
    cursor1.execute(string1,(stock_id))
    # string3 = "DELETE from doctor where doc_id=?;"
    # cursor1.execute(string3,(idx))
    connection.commit()
