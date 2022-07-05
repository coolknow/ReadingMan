from flask import Flask, request, make_response
from flask_cors import cross_origin
from flask import jsonify
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='localhost',#打开数据库链接
    port=3306,
    user='root',
    password='Hu6012493!',
    database='test'
)


@app.route('/login', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def login():
    print('receive')
    # TODO、审核用户名和密码是否符合要求，返回判断结果，并将用户信息存储在前端
    username = request.form.get('username')
    password = request.form.get('pwd')
    print("username: " + str(username))
    print("password: " + str(password))

    cursor = db.cursor();
    sql = "SELECT * FROM test.user WHERE userName = '%s';" % (username)
    cursor.execute(sql)
    data = cursor.fetchone()
    # data[0] : userName
    # data[1] : phone
    # data[2] : email
    # data[3] : password
    # data[4] : uploadRight
    # data[5] : vip
    print(data[0])
    response = make_response(jsonify({'pass':True,'username':username,'password':password}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    return response


@app.route('/register', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def register():
    # TODO 审核用户信息，并返回注册结果，如果不成功则提示重来，如果成功则跳转主页
    return {}


@app.route('/resource', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def resource():
    # TODO 判断用户请求资源的种类，并返回相应的资源数据
    return {}


@app.route('/upload', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def upload():
    # TODO 接受资源数据，并存储在数据库中
    return {}


@app.route('/download', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def download():
    # TODO 获取资源数据请求，并从数据库中调取相应的数据资源返回给前端
    return {}


@app.route('/right', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def right():
    # TODO 在用户申请上传资格的时候检查是否符合条件（互动指数+vip）
    return {}


@app.route('/vip', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def vip():
    # TODO 模拟充值vip，修改数据库，并返回结果到前端
    return {}


@app.route('/like', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def like():
    # TODO 根据 书名 和 点赞/取消点赞 修改数据库点赞表
    return {}


@app.route('/comment', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def comment():
    # TODO 往评论表里增加数据
    return {}



if __name__ == "__main__":
    app.run(debug=True)


# def test():
#     db = pymysql.connect(host='localhost',#打开数据库链接
#                          port=3306,
#                          user='root',
#                          password='123456',
#                          database='test'
#                          )
#     cursor = db.cursor();
#     cursor.execute("SELECT VERSION()")
#     data =cursor.fetchone()
#     print ("Database version :%s"% data)
#     db.close()
#
# def insertUser(userName,phone,email,password,uploadRight,vip):#向用户表中插入数据
#     db = pymysql.connect(host='localhost',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      database='test'
#                      )
#     cursor = db.cursor();
#     sql="INSERT INTO `test`.`user` (`userName`, `phone`, `email`, `password`, `uploadRight`, `vip`) \
#      VALUES ('%s', '%s', '%s', '%s','%s', '%s');" %\
#         (userName,phone,email,password,uploadRight,vip)
#     try:
#         cursor.execute(sql)
#         db.commit()
#         print("insert successful:)")
#     except:
#         db.rollback()
#         print("insert failed:(")
#     db.close()
#
# def queryUser(userName,password):#查找用户信息表
#     db = pymysql.connect(host='localhost',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      database='test'
#                      )
#     cursor = db.cursor();
#     sql="SELECT * FROM `test`.`user` \
#        WHERE `userName` = '%s' " % (userName)
#     try:
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         if (result[3])==password:
#             print("Correct password")
#         else:
#             print("Wrong password")
#     except:
#         print ("query failed:)")
#     db.close()
#
# #insertUser("yxp","15801186063","162158662@qq,com","123456","1","1")
# queryUser("yxp","123456")
# queryUser("yxp","666666")

#
#
#
# from flask import Flask, render_template, request, redirect, url_for, session,flash
# import pymysql
# # from flask_mysqldb import MySQL
# # import MySQLdb.cursors
# import re
#
#
#
# app = Flask(__name__,template_folder='templates',)
#
# # # 打开数据库连接
# # db = pymysql.connect(host='localhost',
# #                      user='testuser',
# #                      password='test123',
# #                      database='TESTDB')
# #
# # # 使用 cursor() 方法创建一个游标对象 cursor
# # cursor = db.cursor()
#
# # Change this to your secret key (can be anything, it's for extra protection)
# app.secret_key = '1a2b3c4d5e'
#
# # Enter your database connection details below
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = '*****'
# app.config['MYSQL_PASSWORD'] = '*****'
# app.config['MYSQL_DB'] = '****'
#
# # # Intialize MySQL
# # mysql = MySQL(app)
# @app.route('/index/',methods=['GET','POST'])
# def index():
#     return render_template('bootstrap-4-login-page/index.html',title="Index")
#
# # http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
# @app.route('/pythonlogin/', methods=['GET', 'POST'])
# def login():
# # Output message if something goes wrong...
#     # Check if "username" and "password" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']
#         # Check if account exists using MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
#         # Fetch one record and return result
#         account = cursor.fetchone()
#                 # If account exists in accounts table in out database
#         if account:
#             # Create session data, we can access this data in other routes
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             # Redirect to home page
#             return redirect(url_for('home'))
#         else:
#             # Account doesnt exist or username/password incorrect
#             flash("Incorrect username/password!", "danger")
#     return render_template('auth/login.html',title="Login")
#
#
#
# # http://localhost:5000/pythinlogin/register
# # This will be the registration page, we need to use both GET and POST requests
# @app.route('/pythonlogin/register', methods=['GET', 'POST'])
# def register():
#     # Check if "username", "password" and "email" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#                 # Check if account exists using MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         # cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
#         cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )
#         account = cursor.fetchone()
#         # If account exists show error and validation checks
#         if account:
#             flash("Account already exists!", "danger")
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             flash("Invalid email address!", "danger")
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             flash("Username must contain only characters and numbers!", "danger")
#         elif not username or not password or not email:
#             flash("Incorrect username/password!", "danger")
#         else:
#         # Account doesnt exists and the form data is valid, now insert new account into accounts table
#             cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username,email, password))
#             mysql.connection.commit()
#             flash("You have successfully registered!", "success")
#             return redirect(url_for('login'))
#
#     elif request.method == 'POST':
#         # Form is empty... (no POST data)
#         flash("Please fill out the form!", "danger")
#     # Show registration form with message (if any)
#     return render_template('auth/register.html',title="Register")
#
# # http://localhost:5000/pythinlogin/home
# # This will be the home page, only accessible for loggedin users
#
# @app.route('/pythonlogin/home')
# def home():
#     # Check if user is loggedin
#     if 'loggedin' in session:
#         # User is loggedin show them the home page
#         return render_template('home/home.html', username=session['username'],title="Home")
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))
#
#
# @app.route('/pythonlogin/profile')
# def profile():
#     # Check if user is loggedin
#     if 'loggedin' in session:
#         # User is loggedin show them the home page
#         return render_template('auth/profile.html', username=session['username'],title="Profile")
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))
#
# if __name__ =='__main__':
# 	app.run(debug=True)
