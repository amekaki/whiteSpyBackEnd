import json
import time

from flask import Blueprint, request
import asyncio

from model.chatTaskDB import getOnTasks
from model.telegramDB import getAllUserId
from server.authServer import verify_bearer_token
from server.botserver import getAllTGBot, getAllQQBot
from server.chatTaskServer import getAllInTask
from server.teleGramServer import getGroupsBySearchQuery, getGroupRecord, insertGroup, getAllGroupServer, getAllUser, \
    getUserInfo, insertGroyprandam, deleteGroups, getAllUserServer, sendMessToUser, startChatList, \
    getGroupsBySearchQueryTelethon, insertUser, getGroupLiveness, getGroupPersonType, getGroupInfo
from util.telegramUtil import getGroup,sendToUser,getGroupChattingRecords
telegram=Blueprint("telegram", __name__)

@telegram.route('/test')
def ttest():
    asyncio.run(getGroup("+8618956778851"))
    return "OK"
@telegram.route('/sendMessage',methods=['post'])
def sendToOneUser():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    id = req['userId']
    sendMessToUser(id)
    return "OK"
@telegram.route('/startChatList',methods=['post'])
def sendToMangUser():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    userList = req['userList']
    groupId = req['groupId']
    startChatList(userList,groupId)
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
@telegram.route('/searchGroup2',methods=['post'])
def sssg():
    req = json.loads(request.get_data(as_text=True))
    # token = request.headers['token']
    # author = verify_bearer_token(token)
    print("req",req)
    searchQuery=req['searchQuery']
    searchResult=getGroupsBySearchQueryTelethon(searchQuery)
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
    # groupId=int(req['groupId'])
    groupId = req['groupId']
    insertGroup(groupId)
    return "OK"
@telegram.route('/getAllGroups')
def gag():
    result=getAllGroupServer()
    return json.dumps(result)
@telegram.route('/getAllUsers')
def gaun():
    result=getAllUserServer()
    return json.dumps(result)
@telegram.route('/getUserTypeByGroup',methods=['get'])
def ddcdsvs():
    # req = json.loads(request.get_data(as_text=True))
    # print("req",req)
    # groupId=int(req['groupId'])
    groupId=1150151073
    result=getGroupPersonType(groupId)
    return json.dumps(result)
@telegram.route('/getAllUserByGroup',methods=['post'])
def gubg():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    groupId=int(req['groupId'])
    result=getAllUser(groupId)
    return json.dumps(result)
@telegram.route('/getAllUserIds',methods=['get'])
def ssfids():
    res=getAllUserId()
    return json.dumps(res)
@telegram.route('/getUserInfoById',methods=['post'])
def guig():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)
    userId=int(req['userId'])
    result=getUserInfo(userId)
    return json.dumps(result)
@telegram.route('/addGroup',methods=['post'])
def addGroup():
    req = json.loads(request.get_data(as_text=True))
    print("req",req)

    return "OK"
@telegram.route('/iii',methods=['post'])

def iii():
    insertGroyprandam()
    return "OK"
@telegram.route('/deleteGroups',methods=['post'])

def dgbid():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    ids = req['groupIds']
    deleteGroups(ids)
    return "OK"
@telegram.route('/getTasks',methods=['post'])

def gettaskss():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    type = req['type']
    return json.dumps(getAllInTask(type))

@telegram.route('/getgroupById',methods=['post'])
def gginfoByID():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    id = req['id']
    return json.dumps(getGroupInfo(id))
@telegram.route('/getTGBots',methods=['get'])
def getTGBOTS():
    return json.dumps(getAllTGBot())
@telegram.route('/getQQBots',methods=['get'])
def getTQQQBOTS():
    return json.dumps(getAllQQBot())
@telegram.route('/insertUser',methods=['POST'])
def getinseruser():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    username = req['username']
    insertUser(username)
    return "OK"
@telegram.route('/getGroupLiveness',methods=['POST'])
def getissser():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    groupId = req['groupId']
    getGroupLiveness(groupId)
    return "OK"
