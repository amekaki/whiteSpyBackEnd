from model.messageDB import getMsgLogById


def getMessageByUserId(userId):
    messages=getMsgLogById(userId)
    for msg in messages:
        if msg.isSender==1:
            user=0
    return 1