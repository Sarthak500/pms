def createConnection():
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection
def buy_stock(buy_price,quantity,stock_id,user_id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "insert into Buytransaction (buy_price,buy_date,quantity,stock_id,user_id) values (?,curdate(),?,?,?) ;"
    cursor1.execute(query1,(buy_price,quantity,stock_id,user_id))
    query2='SELECT MAX(trans_id) FROM Buytransaction;'
    cursor1.execute(query2)
    id=cursor1.fetchall()[0][0]
    # query2 = "SELECT LAST_INSERT_ID(trans_id) from Buytransaction ;"
    # cursor1.execute(query2)
    # id=cursor1.fetchall()[0][0]
    # print(id)
    # print(1001)
    query3= "insert into portfoliolisting values (?,?,?,?);"
    cursor1.execute(query3,(user_id,stock_id,id,quantity))
    query4="update Normal_user set cash=cash-{} where user_id={};".format((buy_price*quantity),user_id)
    cursor1.execute(query4)
    #update portfolio cash
    connection.commit()
# buy_stock(100,10,1,3)
def sell_stock(sell_price,quantity,stock_id,user_id,pl_id):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1 = "insert into Selltransaction (sell_price,sell_date,quantity,stock_id,user_id,pl_id) values (?,curdate(),?,?,?,?) ;"
    cursor1.execute(query1,(sell_price,quantity,stock_id,user_id,pl_id))
    query2="update Normal_user set cash=cash+{} where user_id={};".format((sell_price*quantity),user_id)
    cursor1.execute(query2)
    query3="select quantity from Portfoliolisting where stock_id=? and user_id=? and pl_id=?;"
    cursor1.execute(query3,(stock_id,user_id,pl_id))
    value = cursor1.fetchall()
    #print(value[0])
    if len(value) > 0:
        if quantity == value[0][0]:
            query4="delete from Portfoliolisting where stock_id=? and user_id=? and pl_id=?;"
            cursor1.execute(query4,(stock_id,user_id,pl_id))
        elif quantity < value[0][0]:
            query4="update Portfoliolisting set quantity=quantity-? where stock_id=? and user_id=? and pl_id=?;"
            cursor1.execute(query4,(quantity,stock_id,user_id,pl_id))
        else:
            return 0
    else:
        return 0
    #this if else is not necessary
    connection.commit()





