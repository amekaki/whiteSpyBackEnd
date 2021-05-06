from model.modelDB import *


def checkGroup(groupId):
    groupCheck = telegramGroup.query.filter_by(id=groupId).first()
    return groupCheck


def checkUser(id):
    userCheck = telegramUser.query.filter_by(id=id).first()
    return userCheck


def insertSingleGroup(id, title, photo, username, date):
    group = telegramGroup(id, title, photo, username, date)
    db.session.add(group)
    db.session.commit()
    return id


def insertSingleUser(id, first_name, last_name, photo, username, phone):
    user = telegramUser(id, first_name, last_name, photo, username, phone)
    db.session.add(user)
    db.session.commit()
    return id


def insertGroupUser(groupId, userId):
    db.session.execute('INSERT INTO telegramGroupUser VALUES ({},{})'.format(groupId, userId))


def checkGroupUser(groupId, userId):
    return list(
        db.session.execute('SELECT *  from telegramGroupUser where groupId ={} and  userId={}'.format(groupId, userId)))


def getAllGroup():
    groups=telegramGroup.query.filter_by().all()
    return groups

def getAllUserByGroup(groupId):
    print(groupId)
    sql='SELECT userId  from telegramGroupUser where groupId ={} '.format(groupId)
    userResults=list(db.session.execute(sql))
    users=[]
    for userResult in userResults:
        userId=userResult.userId
        user=telegramUser.query.filter_by(id=userId).first()
        users.append(user)
    return users

def getUserById(userId):
    user=telegramUser.query.filter_by(id=userId).first()
    return user


