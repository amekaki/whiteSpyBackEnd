import json
import os
from flask import Blueprint, request
from server.authServer import create_token, verify_bearer_token, checkUser, registeUser

auth = Blueprint("auth", __name__)

@auth.route('/getPost')
def test():
    return request.args['location']

@auth.route('/testToken', methods=['get'])
def testT():
    phoneNumber = request.args.get('phoneNumber', None)
    password = request.args.get('password', None)
    return json.dumps(checkUser(phoneNumber, password))


@auth.route('/loginByPassword', methods=["post"])
def loginByPassword():
    req = json.loads(request.get_data(as_text=True))
    phoneNumber = req['phoneNumber']
    password = req['password']
    return json.dumps(checkUser(phoneNumber, password))


@auth.route('/registe', methods=['post'])
def registeFun():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    phoneNumber = req['phoneNumber']
    password = req['password']
    userName = req['userName']
    return json.dumps(registeUser(phoneNumber, password, userName))


@auth.route('/updateUserInfo', methods=['POST'])
def updateUserInfo():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)


@auth.route('/uploaderAvatar', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        token = request.headers["token"]
        postfix = f.content_type.split("/")[1]
        verify_bearer_token(token)
        print(f.content_type, type(f.content_type))
        filename = verify_bearer_token(token) + "." + postfix
        print(filename)
        UPLOAD_FOLDER = 'static\\img\\headPortrait\\'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER) + filename
        print(file_dir)
        f.save(file_dir)
        return 'file uploaded successfully'
