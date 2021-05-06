import asyncio

from model.modelDB import telegramGroup
from model.telegramDB import insertSingleGroup, checkGroup, checkUser, insertSingleUser, insertGroupUser, \
    checkGroupUser, getAllGroup, getAllUserByGroup, getUserById
from util.telegramUtil import getGroupListInfo, getGroupChattingRecords, getGroupInfo, getGroupUser


def getGroupsBySearchQuery(searchQuery):
    resultList = []
    if searchQuery == '1':
        groupNameList = ["@sim114", '@dajianwangzhan']
    if searchQuery == '2':
        groupNameList = ['@dajianwangzhan', "@sim114"]
    groupList = asyncio.run(getGroupListInfo("+8618956778851", groupNameList))
    for groupDict in groupList:
        groupInfo = groupDict['group']
        path = groupDict['path']
        group = telegramGroup(groupInfo.id, groupInfo.title, path, groupInfo.username, groupInfo.date)
        resultList.append(group.to_json())
    return resultList


def getGroupRecord(groupName):
    result = asyncio.run(getGroupChattingRecords("+8618956778851", groupName))
    print(result, type(result))
    return result


def insertGroup(groupId):
    checkg = checkGroup(groupId)
    if checkg:
        print("已存在")
    else:
        group, groupImgPath = asyncio.run(getGroupInfo("+8618956778851", groupId))
        insertSingleGroup(group.id, group.title, groupImgPath, group.username, group.date)
        print(group.id, group.title, groupImgPath, group.username, group.date)
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
            insertSingleUser(userInfo.id, userInfo.first_name, userInfo.last_name, imgPath, userInfo.username,
                             userInfo.phone)
        if checkGroupUser(groupId, userInfo.id):
            print("关系已存在", checkGroupUser(groupId, userInfo.id))
        else:
            insertGroupUser(groupId, userInfo.id)
    return groupId


def getAllGroupServer():
    groups = getAllGroup()
    groupsJson = []
    for group in groups:
        groupsJson.append(group.to_json())
    return groupsJson


def getAllUser(groupId):
    users = getAllUserByGroup(groupId)
    print("users", users)
    usersJson = []
    for user in users:
        print(user)
        usersJson.append(user.to_json())
    return usersJson


def getUserInfo(userId):
    user = getUserById(userId)
    return user.to_json()
