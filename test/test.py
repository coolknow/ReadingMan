from flask import Flask, request, make_response
from flask_cors import cross_origin
from flask import jsonify


app = Flask(__name__)


@app.route('/test/',methods=['POST','GET'])
# @cross_origin(origins="http://127.0.0.1:9528") # 设置可以访问的前端端口
def test():
    print("receive")
    data = request.form.get('')
    print(data)
    response = make_response(jsonify({'a':'aprime','b':'bprime'}))
    response.headers["Access-Control-Allow-Origin"] = 'http://127.0.0.1:9528'	# 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST,GET'	# 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'	# 允许的请求header
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    return response


if __name__ == '__main__':
    app.run(debug=True)
