from flask import Flask
from flask_cors import cross_origin
from flask import jsonify


app = Flask(__name__)


@app.route('/test/',methods=['POST','GET'])
@cross_origin(origins="http://127.0.0.1:3000") # 设置可以访问的前端端口
def test():
    print("receive")
    return jsonify({'a':'aprime','b':'bprime'})


if __name__ == '__main__':
    app.run(debug=True)
