from model.modelDB import *
def getMsgLogById(id):
    result=db.session.query(Message).filter_by(senderId=id).order_by(Message.createTime).all()
    # result=Message.query.filter_by(senderId=id).all()
    return result