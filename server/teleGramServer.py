import asyncio
import random
import re

from model.modelDB import telegramGroup
from model.telegramDB import insertSingleGroup, checkGroup, checkUser, insertSingleUser, insertGroupUser, \
    checkGroupUser, getAllGroup, getAllUserByGroup, getUserById, deleteGroup, getAllUserById, getUsertype, getGroupById
from server.chatTaskServer import addTask
from util.telegramUtil import getGroupListInfo, getGroupChattingRecords, getGroupInfo, getGroupUser, sendMessage, \
    sendMessageToUserList, getGroupInfoQuery
from   util.telegramUtil import getUserInfo as getUserInfo2
import datetime
def getGroupLiveness(groupId):
    time=['7-19', '7-20', '7-21', '7-22', '7-23', '7-24', '7-25']
    dataAll=[27, 30, 17, 25, 23, 30,28]
    dataSIM=[25, 28, 16, 20, 21, 29, 27]
    return {"time":time,"dataAll":dataAll,"dataSIM":dataSIM}
def getGroupsBySearchQuery(searchQuery):
    resultList = []
    if searchQuery == '1':
        groupNameList = ["@sim114", '@dajianwangzhan']
    if searchQuery == '2':
        groupNameList = ['@dajianwangzhan', "@sim114"]
    if searchQuery == '注册卡':
        # groupNameList = ["@sim114"]
        groupNameList = ["@shiminghao", "@G_Voice", "@ppayp", "@vxfzzc", "@wxzfbhao", "@sim114"]
    groupList = asyncio.run(getGroupListInfo("+8618956778851", groupNameList))
    for groupDict in groupList:
        groupInfo = groupDict['group']
        path = groupDict['path']
        group = telegramGroup(groupInfo.id, groupInfo.title, path, groupInfo.username, groupInfo.date)
        resultList.append(group.to_json())
    return resultList
def getGroupsBySearchQueryTelethon(searchQuery):
    resultList = []
    groupList = asyncio.run(getGroupInfoQuery("+8618956778851",searchQuery))
    for groupDict in groupList:
        groupInfo = groupDict['group']
        path = groupDict['path']
        group = telegramGroup(groupInfo.id, groupInfo.title, path, groupInfo.username, groupInfo.date)
        resultList.append(group.to_json())
    return resultList
def startChatList(userList,groupId):
    asyncio.run(sendMessageToUserList("+8618956778851",userList,"出卡吗"))
    print(userList)
    for user in userList:
        addTask(user, groupId, "Telegram")
    return "OK"
def getGroupRecord(groupName):
    result = asyncio.run(getGroupChattingRecords("+8618956778851", groupName))
    print(result, type(result))
    return result
def sendMessToUser(id):
    result = asyncio.run(sendMessage("+8618956778851",id,"出卡吗"))
    return "OK"
def getGroupPersonType(groupId):
    res=getUsertype(groupId)
    return [
                {"value": res.count("UNKNOWN"), "name": '未知'},
                {"value": res.count("SIM"), "name": 'SIM卡'},
                {"value":  res.count("CODE"), "name": '接码'},
                {"value":  res.count("ACCOUNT"), "name": '账号'}
              ]
    # TODO 获取成员类型分布
def fuzzyMatch(s,key):
    s=str(s)
    pattern='.*'+key+'.*'
    result=re.findall(pattern,s)
    # print("result",result)
    if(len(result)!=0):
        print(len(result),"关键词key",key, "匹配文字", s)
        return True
    else:
        return False
def insertGroup(groupName):
    checkg = checkGroup(groupName)
    group, groupImgPath = asyncio.run(getGroupInfo("+8618956778851", groupName))
    groupId = group.id
    if checkg:
        print("已存在")
    else:
        insertSingleGroup(group.id, group.title, groupImgPath, group.username, group.date)
        print(group.id, group.title, groupImgPath, group.username, group.date)
        groupId=group.id
    users = asyncio.run(getGroupUser("+8618956778851", groupId))
    for user in users:
        # for i in range(5):
        #     user=users[i]
        print(user)
        userInfo = user["userInfo"]
        imgPath = user["imgPath"]
        checku = checkUser(userInfo.id)
        if checku:
            print("用户已存在", checku)
        else:
            classes = [['卡', '电信', '移动', 'sim', '三网'], ['号', '账号'], ['码', '验证', '短信']]
            labels = ['SIM', 'ACCOUNT', 'CODE']
            defaultLabel = 'UNKNOWN'
            #TODO 判断用户类型
            insertSingleUser(userInfo.id, userInfo.first_name, userInfo.last_name, imgPath, userInfo.username,
                             userInfo.phone)
        if checkGroupUser(groupId, userInfo.id):
            print("关系已存在", checkGroupUser(group.id, userInfo.id))
        else:
            insertGroupUser(groupId, userInfo.id)
    return groupId
def insertUser(username):
    userInfo = asyncio.run(getUserInfo2("+8618956778851", username))
    imgPath='static\\img\\userImg\\{}.jpg'.format(userInfo.id)
    insertSingleUser(userInfo.id, userInfo.first_name, userInfo.last_name, imgPath, userInfo.username,
                     userInfo.phone)

def getAllGroupServer():
    groups = getAllGroup()
    groupsJson = []
    for group in groups:
        groupsJson.append(group.to_json())
    #     g=group
    # for i in range(120):
    #     groupsJson.append(g)
    return groupsJson
def getAllUserServer():
    groups = getAllUserById()
    groupsJson = []
    for group in groups:
        groupsJson.append(group.to_json())
    #     g=group
    # for i in range(120):
    #     groupsJson.append(g)
    return groupsJson

def getAllUser(groupId):
    users = getAllUserByGroup(groupId)
    usersJson = []
    for user in users:
        usersJson.append(user.to_json())
    usersJson=usersJson[::-1]
    return usersJson

def getGroupInfo(id):
    group = getGroupById(id)
    return group.to_json()
def getUserInfo(userId):
    user = getUserById(userId)
    return user.to_json()

def generate_random_str(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str
def deleteGroups(ids):
    for id in ids:
        deleteGroup(id)
def insertGroyprandam():
    id0=1946131751
    for i in range(120):
        id=id0+i
        title=generate_random_str(6)
        username = generate_random_str(6)
        insertSingleGroup(id, title, "static/img/headPortrait/2.jpg", username,datetime.datetime.now())
