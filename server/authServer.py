import jwt
import time

from model.userDB import getUserByPhoneNumberAndPassword, getUserByPhoneNumber, insertUser

def registeUser(phoneNumber, password, username):
    if getUserByPhoneNumber(phoneNumber):
        return {'code': 500, 'msg': "手机号已注册"}
    else:
        insertUser(phoneNumber, password, username)
        return {'code': 200, 'msg': "注册成功"}


def checkUser(phoneNumber, password):
    if getUserByPhoneNumberAndPassword(phoneNumber, password):
        return {'code': 200, 'msg': create_token(phoneNumber)}
    else:
        return {'code': 500, 'msg': "用户名或密码错误"}


# 使用 sanic 作为restful api 框架
def create_token(phoneNumber):
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "phoneNumber": phoneNumber
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token


def verify_bearer_token(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    return payload['phoneNumber']
