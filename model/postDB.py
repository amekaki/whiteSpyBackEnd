from pymysql.converters import escape_string

from model.modelDB import *
import datetime
def getPost(location,type):
    if location is not None:
        if type is not None:
            return list(Post.query.filter_by(location=location,type=type))
        else:
            return list(Post.query.filter_by(location=location))
    else:
        return list(Post.query.filter_by())
def getPostByID(postID):
    # print("postID",postID,Post.query.filter_by(postID=postID).first().to_json())
    return Post.query.filter_by(postID=postID).first()

def InsertPost(author,content,location,type,cover,header):
    print(header)
    post=Post(author,content,location,type,cover,None,datetime.datetime.now(),header)
    db.session.add(post)
    db.session.commit()
    return post.postID