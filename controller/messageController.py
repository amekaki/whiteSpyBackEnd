from flask import Blueprint, request
import json

from server.msgServer import getMessageByUserId

msg=Blueprint("msg", __name__)

@msg.route('/getMsgLogById',methods=['post'])
def gmbi():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    id=req['userId']
    print(id)
    result=getMessageByUserId(id)
    print(result)
    return json.dumps(result)

