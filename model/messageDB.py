from model.modelDB import *
def getMsgLogById(id):
    result=Message.query.filter_by(senderId=id).all()
    return result