def createConnection():
    import mysql.connector
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection
def update_stock(stock_symbol,cur_price,cur_date,volume):
    connection = createConnection()
    cursor1 = connection.cursor(prepared=True)
    query1="select cur_price,stock_id from Stock where stock_symbol='{}' ;".format(stock_symbol)
    cursor1.execute(query1)
    value = cursor1.fetchall()
    cur_price_old=value[0][0]
    stock_id=value[0][1]
    query2="update Stock set cur_price=? , volume=? , cur_date=? where stock_id=? ;"
    cursor1.execute(query2,(cur_price,volume,cur_date,stock_id))
    # connection.commit()
    #stock symbol can be used alternatively
    #update portfolio cash

    # query3="select user_id,sum(quantity) from (select * from pms.Portfoliolisting where stock_id= ? ) as pls group by user_id,stock_id;"
    query3="select user_id,holdings from us_total where stock_id= ? ;"
    cursor1.execute(query3,(stock_id,))
    value = cursor1.fetchall()
    diff=cur_price-cur_price_old
    for row in value:
        user_id=row[0]
        no=row[1]
        updation_val=no*diff
        query4 = "update Normal_user set worth=worth+? where user_id = ? ;"
        cursor1.execute(query4,(updation_val,user_id))
        # connection.commit()
        # print(row[0],row[1])
        # connection.commit()
        # my_dict = {'f_name' : row[0],'user_id':row[1],'contact':row[2],'location':row[3], 'email':row[4]}
        # list1.append(my_dict)
    # return list1
    connection.commit()
# update_stock("BMRN", 84.1316, "2021-01-11",2696854)
