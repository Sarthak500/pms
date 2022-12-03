import mysql.connector
def createConnection():
    
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection

# Fetches information from table


def getUserInfo(user_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select user_id,username,email,passwd,surname,address,mobile,dob,worth,cash from normal_user where user_id = {}; ".format(user_id)
    #or username?? for input
    cursor1.execute(string)
    value = cursor1.fetchall()
    # print(value)
    #print("The user id is ------> " + str(user_idx))
    my_dict = {'user_id' : value[0][0],'username':value[0][1],'email':value[0][2],'passwd':value[0][3], 'surname':value[0][4], 'address':value[0][5],'mobile':value[0][6],'dob':value[0][7],'worth':value[0][8],'cash':value[0][9]}
    # connection.commit()
    # print("Dictionary ---->" + str(my_dict))
    # print(my_dict)
    return my_dict
# getUserInfo(2)
def getAdminInfo(admin_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    # string = "select name,admin_id,email,password from Admin where admin_id = ?;"
    # cursor1.execute(string,(admin_id,))
    string = "select admin_id,username,passwd,surname from Admin_user where admin_id = {};".format(admin_id)# or username?
    cursor1.execute(string)
    value = cursor1.fetchall()
    my_dict = {'admin_id' : value[0][0],'username':value[0][1],'passwd':value[0][2],'surname':value[0][3]}
    # connection.commit()
    return my_dict

def getStockInfo(stock_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "select stock_id,stock_name,stock_symbol,cur_price,cur_date from Stock where stock_id = {};".format(stock_id)# or stock symbol
    cursor1.execute(string)
    value = cursor1.fetchall()
    my_dict = {'stock_id' : value[0][0],'stock_name':value[0][1],'stock_symbol':value[0][2],'cur_price':value[0][3],'cur_date':value[0][4]}
    # connection.commit()
    return my_dict

def getUserTable():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select user_id,username,surname,worth from Normal_user ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    #print(str(value))
    for row in value:
        #print(str(row))
        my_dict = {'user_id' : row[0],'username':row[1],'surname':row[2],'worth':row[3]}
        list1.append(my_dict)
    return list1
def getStockTable():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select stock_id,stock_name,stock_symbol,cur_price,cur_date,volume from Stock ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    #print(str(value))
    for row in value:
        #print(str(row))
        my_dict = {'stock_id' : row[0],'stock_name':row[1],'stock_symbol':row[2],'cur_price':row[3], 'cur_date':row[4],'volume':row[5]}
        list1.append(my_dict)
    return list1

def getTop10UsersTable():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select user_id,username,surname,worth from top_users limit 10 ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    #print(str(value))
    for row in value:
        #print(str(row))
        my_dict = {'user_id' : row[0],'username':row[1],'surname':row[2],'worth':row[3]}
        list1.append(my_dict)
    return list1

def getTopStocksTable():
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select stock_id,stock_name,stock_symbol,User_count,cur_price from top_stocks limit 10 ;"
    cursor1.execute(string)
    value = cursor1.fetchall()
    #print(str(value))
    for row in value:
        #print(str(row))
        my_dict = {'stock_id' : row[0],'stock_name':row[1],'stock_symbol':row[2],'user_count':row[3],'cur_price':row[4]}
        list1.append(my_dict)
    return list1
# print(getTopStocksTable())

def getPortfolioListingTable(user_id):
    connection = createConnection()
    cursor1 = connection.cursor()
    list1 = []
    string = "select stock_symbol,stock_name,stock_id,cur_price,cur_date,quantity,buy_date,buy_price,pl_id,user_id from complete_pl where user_id = {}; ".format(user_id)
    #or username?? for input
    cursor1.execute(string)
    value = cursor1.fetchall()
    for row in value:
        #print(str(row))
        my_dict = {'stock_symbol' : row[0],'stock_name':row[1],'stock_id':row[2],'cur_price':row[3],'cur_date':row[4],'quantity':row[5],
        'buy_date':row[6],'buy_price':row[7],'pl_id':row[8],'user_id':row[9],'diff':((row[3]-row[7])*row[5])}
        list1.append(my_dict)
    return list1