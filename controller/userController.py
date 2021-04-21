from flask import Blueprint, request

from server.authServer import verify_bearer_token
from server.userServer import getUserInfo

user=Blueprint("user", __name__)

@user.route('/getUserInfo',methods=['get'])
def gUserInfo():
    token=request.headers['token']
    userPhonenumber = verify_bearer_token(token)
    return getUserInfo(userPhonenumber)