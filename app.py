import json
import os

from flask import Flask
from flask import send_from_directory, request
# from flask_redis import FlaskRedis
import time

from werkzeug.utils import secure_filename

from controller.authController import auth
from controller.messageController import msg
from controller.showController import show
from controller.userController import user
from controller.telegramController import telegram
from model import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# redis_client = FlaskRedis()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:eroch123@112.126.102.75:3306/whiteSpy?charset=utf8mb4'  # 指定数据库地址、用户名、密码
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] =-1
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True}
app.config['REDIS_URL'] = "redis://:eroch123@192.168.197.145:6379/0"
db.init_app(app)
# redis_client.init_app(app)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(telegram, url_prefix='/telegram')
app.register_blueprint(show, url_prefix='/show')
app.register_blueprint(msg, url_prefix='/msg')



@app.route('/')
def hello_world():
    # redis_client.set('potato', "value")
    userId = '123'
    userData = {'key1': 'value1', 'key2': "value2"}
    mark_dyn_data(userId, userData)
    print(json.loads(str(userData)))
    return 'Hello World!'


@app.route("/download", methods=['GET'])
def index():
    filepath = request.args.get('filepath')
    l = filepath.split("/")
    path = ""
    if (len(l) != 1):
        for i in range(len(l) - 2):
            path = path + l[i] + "/"
        path = path + l[-2]
    filename = l[-1]
    return send_from_directory(path, filename, as_attachment=True)


@app.route('/uploaderCover', methods=['GET', 'POST'])
def uploaders():
    if request.method == 'POST':
        file = request.files['file']
        filepath = request.form.get("filepath")
        filename = request.form.get("filepath")
        l = filepath.split("/")
        path = ""
        if (len(l) != 1):
            for i in range(len(l) - 2):
                path = path + l[i] + "/"
            path = path + l[-2]
        # filename = l[-1]
        file.save(path, filename)
        return 'file uploaded successfully'


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join("static/img/postCover/", f.filename))
        return 'file uploaded successfully'


# @app.route('/uploader', methods=['POST'])
# def uploader():
#     if request.method == 'POST':
#         print("POST")
#         print("req",request.form)
#     else:
#         print("else")
# print("111")
# file = request.files['file']
# print("file", file)
# # filepath = request.args.get("filepath")
#
# # print("filepath",filepath)
# # l = filepath.split("/")
# # path = ""
# # if (len(l) != 1):
# #     for i in range(len(l) - 2):
# #         path = path + l[i] + "/"
# #     path = path + l[-2]
# # filename = l[-1]
# # print(path, filename)
# # file.save(path, filename)
# return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()


