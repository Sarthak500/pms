import mysql.connector
def createConnection():
    
    connection=mysql.connector.connect(host='localhost',
                                user='hb',
                                passwd='mysqluserpassword',
                                database='pms',
                                auth_plugin='mysql_native_password')
    print(connection.connection_id)
    return connection
def insertToAdmin(username,password,surname):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "insert into admin_user (username,passwd,surname) values('{}','{}','{}');".format(username,password,surname)
    # string = "insert into Admin values (?,?,?,?);"
    cursor1.execute(string)
    connection.commit()
# insertToAdmin('john007','abcd1234','john')

def insertTouser(username,email,password,surname,location,contact,dob):
    connection = createConnection()
    cursor1 = connection.cursor()
    string = "insert into normal_user (username,email,passwd,surname,address,mobile,dob) values ('{}','{}','{}','{}','{}','{}','{}');".format(username,email,password,surname,location,contact,dob)
    # string = "insert into Client values (?,?,?,?,?,?);"
    # cursor1.execute(string,(name,idx,contact,location,email,password))
    cursor1.execute(string)
    connection.commit()


def insertTostock(stock_name,stock_symbol,cur_price,cur_date,volume):
    connection1 = createConnection()
    cursor1 = connection1.cursor()
    string = "insert into Stock (stock_name,stock_symbol,cur_price,cur_date,volume) values ('{}','{}',{},'{}',{});".format(stock_name,stock_symbol,cur_price,cur_date,volume)
    # string="insert into Stock (stock_name,stock_symbol,cur_price,cur_date,volume) values ('%s','%s',%f,'%s',%d);"%(connection.escape_string(stock_name),stock_symbol,cur_price,cur_date,volume)
    # string = "insert into Client values (?,?,?,?,?,?);"
    # cursor1.execute(string,(name,idx,contact,location,email,password))
    # string="insert into Stock (stock_name,stock_symbol,cur_price,cur_date,volume) values (%s,%s,%f,%s,%d);"

    # cursor1.execute(string,(stock_name,stock_symbol,cur_price,cur_date,volume))
    cursor1.execute(string)
    connection1.commit()

