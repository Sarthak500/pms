######################### Flask Imports ###################################
from flask import Flask
#from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
#from flask import session
import os
###########################################################################
from Functions import getinfo
from Functions import register_new
from Functions import Edit_existing
from Functions import Log_in
from Functions import remove
from Functions import update_stocks
from Functions import transaction
###########################################################################
import datetime
app = Flask(__name__,static_url_path='/static')
#app.secret = os.urandom(24)
###############################################################################

logged_in={'username':"", 'type':"", 'id':""}
editIDfromAdmin = ""
filter_list = []

@app.route('/',methods=['POST','GET'])
def index():
    if(request.method == 'GET'):
        return render_template('index3.html',personal_info = getinfo.getAdminInfo(logged_in['id']),users_info=getinfo.getUserTable() ,stocks_info = getinfo.getStockTable())
    elif(request.method == 'POST'):
        print("Request debug out" + str(request.form))
        return redirect(url_for('index'))



@app.route('/login',methods=['GET','POST'])
def login():
	if(request.method == 'GET'):
		return render_template('login.html')
	elif(request.method == 'POST') :
         if (request.form['submit_button']=='user'):
             username = request.form['user_name']
             password = request.form['user_password']
             result = Log_in.userlogin(username,password)
             if result > 0 :
            #    session['user'] = id
                logged_in['username'] = username
                logged_in['type'] = "user"
                logged_in['id'] = result
                
                print(result)
                return redirect(url_for('user_dashboard'))
             else:
                # flash("Invalid credentials")
                return redirect(url_for('login'))
            
         elif(request.form['submit_button']=='admin'):
             username = request.form['user_name']
             password = request.form['admin_password']
             result = Log_in.adminlogin(username,password)
             print("THE RESULT IS " + str(result))
             if result >0:
            #    session['user'] = id
                logged_in['username'] = username
                logged_in['type'] = "admin"
                logged_in['id'] = result
                return redirect(url_for('index'))
             else:
                #flash("Invalid credentials")
                return redirect(url_for('login'))

@app.route('/register_user',methods=['GET','POST'])
def register_user():
	if(request.method == 'GET'):
		return render_template('register_user.html')
	elif request.method == 'POST' :
           try :
              username = request.form['username']
              surname = request.form['name']
              email = request.form['email']
              password = request.form['password']
              
              contact = request.form['contact']
              location = request.form['address']
              dob=request.form['dob']
              # print(1)
              # print(dob)
              register_new.insertTouser(username,email,password,surname,location,contact,dob)
              return redirect(url_for('login'))
              # print("Done")
              #flash("Account created")
           except Exception as e :
              print(e)
              #flash("Error occured")
              return redirect(url_for('login'))

@app.route('/register_stock',methods=['GET','POST'])
def register_stock():
	if(request.method == 'GET'):
		return render_template('register_stock.html')
	elif request.method == 'POST' :
           try :
              stock_name = request.form['stock_name']
              stock_symbol = request.form['stock_symbol']
              cur_price = request.form['cur_price']
              cur_date = request.form['cur_date']
              register_new.insertTostock(stock_name,stock_symbol,cur_price,cur_date)
              return redirect(url_for('index'))
           except Exception as e :
              print(e)
              return redirect(url_for('index'))

@app.route('/edit_user',methods=['GET','POST'])
def edit_user():
    if(request.method == 'GET'):
        if(logged_in['type'] == "user"):
            return render_template('edit_user.html',personal_info = getinfo.getUserInfo(logged_in['id']))
        elif(logged_in['type'] == "admin"):
            print("Before rendering : " + editIDfromAdmin)
            return render_template('edit_user.html',personal_info = getinfo.getUserInfo(editIDfromAdmin))
    elif(request.method == 'POST'):
        username = request.form['username']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        
        contact = request.form['contact']
        location = request.form['address']
        dob=request.form['dob']
        if(logged_in['type'] == "user"):
           Edit_existing.editUser(logged_in['id'],username,surname,email,contact,password,location,dob)
           return redirect(url_for('user_dashboard'))
        elif(logged_in['type'] == "admin"):
           Edit_existing.editUser(editIDfromAdmin,username,surname,email,contact,password,location,dob)
           return redirect(url_for('index'))

@app.route('/edit_stock',methods=['GET','POST'])
def edit_stock():
    if(request.method == 'GET'):
        if(logged_in['type'] == "admin"):
            print("Before rendering : " + editIDfromAdmin)
            return render_template('edit_stock.html',stock_info = getinfo.getStockInfo(editIDfromAdmin))
    elif(request.method == 'POST'):
        stock_name = request.form['stock_name']
        stock_symbol = request.form['stock_symbol']
        cur_price = request.form['cur_price']
        cur_date = request.form['cur_date']
        if(logged_in['type'] == "admin"):
           Edit_existing.editStock(editIDfromAdmin ,stock_name,stock_symbol,cur_price,cur_date)
           return redirect(url_for('index'))

@app.route('/edit_admin',methods=['GET','POST'])
def edit_admin():
    if(request.method == 'GET'):
        return render_template('edit_admin.html',personal_info=getinfo.getAdminInfo(logged_in['id']))
    elif(request.method == 'POST'):
        username = request.form['username']
        surname = request.form['surname']
        password = request.form['password']
        Edit_existing.editAdmin(logged_in['id'],username,surname,password)
        return redirect(url_for('index'))

@app.route('/user_dashboard',methods=['GET','POST'])
def user_dashboard():
    if(request.method == 'GET'):
        # print(logged_in['id'])
        # personal_info={'user_id': 1, 'username': 'ad1', 'email': 'adams@gmail.com', 'passwd': 'adam1234', 'surname': 'Adams', 'address': 'Pittsfield', 'mobile': '9999912345', 'dob': datetime.date(1984, 10, 3), 'worth': 100000.0, 'cash': 100000.0}
        # print(getinfo.getUserInfo(logged_in['id']),)
        
        return render_template('user_dashboard.html', personal_info = getinfo.getUserInfo(logged_in['id']), portfolio_info= getinfo.getPortfolioListingTable(logged_in['id']),top_stocks_info = getinfo.getTopStocksTable(),top_users_info = getinfo.getTop10UsersTable(),stocks_info = getinfo.getStockTable())
        
        # print(getinfo.getUserInfo(logged_in['id']))
        # return render_template('user_dashboard.html', personal_info = getinfo.getUserInfo(logged_in['id']))
    elif(request.method == 'POST'):
         #print(request.form)
         applied_filters={'column':"", 'value':""}
         global filter_list
         #print("The value ---------------->    " + str(applied_filters))
         filter_in = request.form['filter_input']
         time = request.form['time']
         column = request.form['property']
         if column != "UNSELECTED":
             applied_filters['column'] = column
             applied_filters['value'] = filter_in
             filter_list.append(applied_filters)
             #print("POST REQUEST PROCESSED")
         return render_template('user_dashboard.html', personal_info = getinfo.getUserInfo(logged_in['id']), portfolio_info= getinfo.getPortfolioListingTable(logged_in['id']),top_stocks_info = getinfo.getTopStocksTable(),
                                top_users_info = getinfo.getTop10UsersTable(),stocks_info = getinfo.getStockTable())

@app.route('/removeStock',methods=['GET'])
def removeStock():
    if(request.method == 'GET'):
        stock_id = request.args.get('id');
        remove.removeFromStock(stock_id)
        return redirect(url_for('index'))

@app.route('/removeUser', methods=['GET'])
def removeUser():
    if(request.method == 'GET'):
        id = request.args.get('id')
        remove.removeFromUser(id)
        return redirect(url_for('index'))

@app.route('/editUserfromAdmin', methods=['GET'])
def editUserfromAdmin():
    if(request.method == 'GET'):
        id = request.args.get('id')
        print("The ID from server.py ------>  " + id)
        global editIDfromAdmin
        editIDfromAdmin = id
        return redirect(url_for('edit_user'))

@app.route('/editStockfromAdmin', methods=['GET'])
def editStockfromAdmin():
    if(request.method == 'GET'):
        stock_id = request.args.get('id')
        #print("The ID from server.py ------>  " + id)
        global editIDfromAdmin
        editIDfromAdmin = stock_id
        return redirect(url_for('edit_stock'))

@app.route('/removeFilter', methods=['GET'])
def removeFilter():
    if(request.method == 'GET'):
        global fliter_list
        filter_list = []
        return redirect(url_for('user_dashboard'))

@app.route('/logout', methods=['GET'])
def logout():
    if(request.method == 'GET'):
        global fliter_list
        filter_list = []
        global logged_in
        logged_in['id'] = ""
        logged_in['username'] = ""
        logged_in['type'] = ""
        return redirect(url_for('login'))

@app.route('/buyStocks', methods=['GET','POST'])
def buyStocks():
    if(request.method == 'GET'):
        stock_id = request.args.get('stock_id')
        stock_name = request.args.get('stock_name')
        stock_symbol = request.args.get('stock_symbol')
        user_id=request.args.get('user_id')
        price=request.args.get('price')
        # print(stock_id)
        # print(stock_name)
        # print(stock_symbol)
        # print(user_id)
        # print(price)
        return render_template('buy_stock.html',info={'stock_id':stock_id,'stock_name':stock_name,'stock_symbol':stock_symbol,'user_id':user_id,'price':price})
    if(request.method == 'POST'):
        stock_id = int(request.args.get('stock_id'))
        # stock_name=request.args.get('stock_name')
        # stock_symbol=request.args.get('stock_symbol')
        user_id=int(request.args.get('user_id'))
        price=float(request.args.get('price'))
        
        quantity=int(request.form['quantity'])
        print(stock_id,user_id,price,quantity)
        # print(quantity.type)
        transaction.buy_stock(price,quantity,stock_id,user_id)
        return redirect(url_for('user_dashboard'))
    
# @app.route('/buyStock', methods=['GET'])
# def buyStock():
#     if(request.method == 'GET'):
#         stock_id = request.args.get('stock_id')
#         user_id=request.args.get('user_id')
#         price=request.args.get('price')
#         quantity=request.args.get('quantity')
#         transaction.buy_stock(price,quantity,stock_id,user_id)
#         return redirect(url_for('user_dashboard'))

@app.route('/sellStocks', methods=['GET','POST'])
def sellStocks():
    if(request.method == 'GET'):
        stock_id = int(request.args.get('stock_id'))
        stock_name = request.args.get('stock_name')
        stock_symbol = request.args.get('stock_symbol')
        user_id=int(request.args.get('user_id'))
        price=float(request.args.get('price'))
        trans_id = int(request.args.get('trans_id'))
        max_quantity=request.args.get('quantity')
        print('max=',max_quantity)
        return render_template('sell_stock.html',info={'stock_id':stock_id,'stock_name':stock_name,'stock_symbol':stock_symbol,'user_id':user_id,'price':price,'trans_id':trans_id,'max':max_quantity})
    elif(request.method=='POST'):   
        stock_id = int(request.args.get('stock_id'))
        # stock_name=request.args.get('stock_name')
        # stock_symbol=request.args.get('stock_symbol')
        user_id=int(request.args.get('user_id'))
        price=float(request.args.get('price'))
        trans_id = int(request.args.get('trans_id'))
        quantity=int(request.form['quantity'])
        print(trans_id)
        print(user_id)
        print(quantity)
        print(stock_id)
        transaction.sell_stock(price,quantity,stock_id,user_id,trans_id)
        print('hello')
        return redirect(url_for('user_dashboard'))

app.run()