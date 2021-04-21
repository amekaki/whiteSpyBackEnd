from model.postDB import getPost, InsertPost
from model.userDB import getUserByPhoneNumber


def getPosts(location=None,type=None):
    postList=getPost(location,type)
    postResult=[]
    for i in postList:
        # setattr(i,'modifiedTime',i.modifiedTime.strftime("%Y-%m-%d-%H"))
        i=i.to_json()
        auth=getUserByPhoneNumber(i['author'])
        i['authorName']=auth.userName
        i['authorheadPortrait']='http://localhost:5000/download?filepath='+auth.headPortrait
        postResult.append(i)
    print("postList",postResult)
    return postResult
def createPost(author, content, location, type, cover, header):
    return InsertPost(author, content, location, type, cover, header)