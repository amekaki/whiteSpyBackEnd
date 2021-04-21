import json
import os
import time

from flask import Blueprint, request

from model.postDB import getPostByID
from server.authServer import verify_bearer_token
from server.postServer import getPosts, createPost

post = Blueprint("post", __name__)


@post.route('/getPost')
def test():
    return request.args['location']


@post.route('/getPosts', methods=["GET"])
def getPostRoute():
    if request.args.get('location', None) is not None:
        location = request.args.get('location', None)
        if request.args.get('type', None) is not None:
            type = request.args.get('type', None)
            resultList = getPosts(type=type, location=location)
        else:
            resultList = getPosts(location=location)
    else:
        resultList = getPosts()
    return json.dumps(resultList)


@post.route('/getPostByPostID', methods=["POST"])
def getPostByPostID():
    req = json.loads(request.get_data(as_text=True))
    postID = req.get("postID")
    print("POSTID", postID)
    return json.dumps(getPostByID(postID).to_json())


@post.route('/createPost', methods=['post'])
def create():
    req = json.loads(request.get_data(as_text=True))
    token = request.headers['token']
    author = verify_bearer_token(token)
    print('heade route', req['header'])
    id = createPost(author, req['content'], req['location'], req['type'], req['cover'], req['header'])

    return str(id)


xx()


@post.route('/uploadPostImg', methods=['post'])
def uploadPostImg():
    if request.method == 'POST':
        f = request.files['file']
        postfix = f.content_type.split("/")[1]
        t = time.time()
        filename = str(round(t)) + "." + postfix
        UPLOAD_FOLDER = 'static/img/postImg/' + filename
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        print(file_dir)
        f.save(file_dir)
        print("dir", UPLOAD_FOLDER)
        return json.dumps({'link': 'http://localhost:5000/download?filepath=' + UPLOAD_FOLDER})


xx()


@post.route('/uploadeCover', methods=['GET', 'POST'])
def uploaderCover():
    if request.method == 'POST':
        f = request.files['file']
        token = request.headers["token"]
        postfix = f.content_type.split("/")[1]
        print(f.content_type, type(f.content_type))
        filename = verify_bearer_token(token) + "." + postfix
        print(filename)
        UPLOAD_FOLDER = 'static/img/postCover/' + f.filename
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        print(file_dir)
        f.save(file_dir)
        print("dir", UPLOAD_FOLDER)
        return UPLOAD_FOLDER
