from flask import Blueprint, request
import asyncio
from util.telegramUtil import getGroup,sendToUser,getGroupInfo
telegram=Blueprint("telegram", __name__)

@telegram.route('/test')
def ttest():
    asyncio.run(getGroup("+8618956778851"))
    return "OK"
@telegram.route('/sendMessage',methods=['post'])
def sendToOneUser():
    asyncio.run(sendToUser("+8618956778851",'+8613681304257', 'Hello, friend!'))
    return "OK"
@telegram.route('/getGroupInfo')
def getGroup():
    return asyncio.run(getGroupInfo("+8618956778851"))