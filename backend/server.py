from flask import Flask, request, make_response, Response
from flask_cors import cross_origin
from flask import jsonify
from dbrelated import *
import pymysql
import os
import uuid

app = Flask(__name__)

db = pymysql.connect(
    host='localhost',#打开数据库链接
    port=3306,
    user='root',
    password='Hu6012493!',
    database='test'
)

UPLOAD_FOLDER = 'resource'

@app.route('/login', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def login():
    print('---- Login ----')
    # TODO、审核用户名和密码是否符合要求，返回判断结果，并将用户信息存储在前端
    username = request.form.get('username')
    password = request.form.get('pwd')
    print("username: " + str(username))
    print("password: " + str(password))
    result = queryUser(username,password,db)
    # cursor = db.cursor();
    # sql = "SELECT * FROM test.user WHERE userName = '%s';" % (username)
    # cursor.execute(sql)
    # data = cursor.fetchone()
    response = make_response(jsonify({'pass':result,'username':username}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response



@app.route('/register', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def register():
    print('---- Register ----')
    # TODO 审核用户信息，并返回注册结果，如果不成功则提示重来，如果成功则跳转主页
    username = request.form.get('username')
    phone = request.form.get('ph')
    email = request.form.get('em')
    password = request.form.get('pwd')
    print("username: " + str(username))
    print("password: " + str(password))
    print("phone: " + str(phone))
    print("email: " + str(email))
    uploadRight = 0
    vip = 0
    # 验证 用户名 / 邮箱 是否都已经注册过
    # 注册新的用户
    result = insertUser(username,phone,email,password,uploadRight,vip,db)
    response = make_response(jsonify({'pass':result,'username':username}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/audio/pcm_mp3/<file_key>')
def stream_mp3(file_key):
    def generate():
        path = 'resource/Kalimba.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


@app.route('/resource/', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def resource():
    # TODO 判断用户请求资源的种类，并返回相应的资源数据
    #id=
    result=queryResource(id,db)#0id,1label,2title,3name,4summary,5type

    return {}


def random_filename(filename):
    ext = os.path.splitext(filename)[-1]
    return uuid.uuid4().hex + ext


@app.route('/uploadfile', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def uploadFile():
    # TODO 接受资源数据，并存储在数据库中
    #username=
    #id=
    #date=
    # insertUpload(username,id,date,db)
    print('---- Upload File ----')
    try:
        file = request.files.get('file')
        print("receive file")
        print(file.filename)
        filename = random_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(os.path.join(app.root_path, filepath))
        print("upload success")
    except:
        print("oh! soemthing wrong")
    response = make_response(jsonify({'fileURL':filepath}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/uploadFilepathToDB', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def uploadFilepathToDB():
    print('---- Upload Filepath to DB ----')
    username = request.form.get('username')
    fileURL = request.form.get('fileURL')
    title = request.form.get('title')
    bookName = request.form.get('bookName')
    booktag = request.form.get('booktag')
    desc = request.form.get('desc')
    print(username)
    print(fileURL[0:15])
    print(title)
    print(bookName)
    print(booktag)
    print(desc)
    date = "2022-07-08"
    insertUpload(username,fileURL[0:15],date,db)
    response = make_response(jsonify({'result':True}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/download', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def download():
    print('---- Download ----')
    # TODO 获取资源数据请求，并从数据库中调取相应的数据资源返回给前端
    username = request.form.get('username')
    id = "resource/2a045e"
    date = "2022-07-08"
    insertDownload(username,id,date,db)#会自动加下载数
    # result = queryResource(id,db)#0id,1label,2title,3name,4summary,5type
    response = make_response(jsonify({'result':True}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/right', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def right():
    print('---- Get Right ----')
    # TODO 在用户申请上传资格的时候检查是否符合条件（互动指数+vip）
    username = request.form.get('username')
    print(username)
    result = queryRight(username,db)#0上传资格1vip
    ans = False
    if(result[0] == 1 and result[1] == 1):
        ans = True
    else:
        ans = False
    response = make_response(jsonify({'result':ans}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/vip', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def vip():
    print('---- Vip ----')
    # TODO 模拟充值vip，修改数据库，并返回结果到前端
    username = request.form.get('username')
    print(username)
    vip='1'
    updatevip(username,vip,db)
    response = make_response(jsonify({'result':True}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response


@app.route('/like', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def like():
    # TODO 根据 书名 和 点赞/取消点赞 修改数据库点赞表
    #username=request.form.get('username')
    #id=request.form.get('id')
    #upValue=request.form.get('upvalue')
    insertUp(username,id,upValue)#会自动更新
    return {}


@app.route('/comment', methods=['GET', 'POST'])
# @cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def comment():
    print('---- Comment ----')
    # TODO 往评论表里增加数据
    username = request.form.get('username')
    content = request.form.get('remark')
    print(username)
    print(content)
    id = "rand"
    result = insertComment(id,username,content,db)#成功为真，失败为假
    if(result):
        updateuploadRight(username,"1",db)
    response = make_response(jsonify({'token':result}))
    # response = make_response(jsonify({}))
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    print('---- ----- ----')
    return response



if __name__ == "__main__":
    app.run(debug=True)

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
