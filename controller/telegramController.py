import json

from flask import Blueprint, request
import asyncio

from server.authServer import verify_bearer_token
from server.teleGramServer import getGroupsBySearchQuery, getGroupRecord, insertGroup, getAllGroupServer, getAllUser, \
    getUserInfo
from util.telegramUtil import getGroup,sendToUser,getGroupChattingRecords
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
    return asyncio.run(getGroupChattingRecords("+8618956778851","@sim114"))

@telegram.route('/searchGroup',methods=['post'])
def sg():
    req = json.loads(request.get_data(as_text=True))
    # token = request.headers['token']
    # author = verify_bearer_token(token)
    print("req",req)
    searchQuery=req['searchQuery']
    searchResult=getGroupsBySearchQuery(searchQuery)
    return json.dumps(searchResult)

@telegram.route('/getGroupChatRecord',methods=['post'])
def gcr():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    groupName=req['groupName']
    result=getGroupRecord(groupName)
    return json.dumps(result)

@telegram.route('/insertGroup',methods=['post'])
def insertG():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    groupId=int(req['groupId'])
    insertGroup(groupId)
    return "OK"
@telegram.route('/getAllGroups')
def gag():
    result=getAllGroupServer()
    return json.dumps(result)

@telegram.route('/getAllUserByGroup',methods=['post'])
def gubg():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    groupId=int(req['groupId'])
    result=getAllUser(groupId)
    return json.dumps(result)

@telegram.route('/getUserInfoById',methods=['post'])
def guig():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    userId=int(req['userId'])
    result=getUserInfo(userId)
    return json.dumps(result)
