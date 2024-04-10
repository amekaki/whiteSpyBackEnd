from model.modelDB import *

def getStatistic(groupId):
    pass
def checkGroupById(id):
    print(id)
    groupCheck = telegramGroup.query.filter_by(id=id).first()
    print("groupCheck",groupCheck)
    if groupCheck:
        return groupCheck.photo
    else:
        return None
def checkGroup(username):
    username=username[1:]
    groupCheck = telegramGroup.query.filter_by(username=username).first()
    print("groupCheck",groupCheck)
    return groupCheck
def deleteGroup(groupId):
    db.session.query(telegramGroup).filter_by(id = groupId).delete()
    db.session.commit()



def checkUser(id):
    userCheck = telegramUser.query.filter_by(id=id).first()
    return userCheck


def insertSingleGroup(id, title, photo, username, date):
    print(id, title, photo, username, date)
    group = telegramGroup(id, title, photo, username, date)
    db.session.add(group)
    db.session.commit()
    return id


def insertSingleUser(id, first_name, last_name, photo, username, phone,label=None):
    user = telegramUser(id, first_name, last_name, photo, username, phone,label)
    db.session.add(user)
    db.session.commit()
    return id


def insertGroupUser(groupId, userId):
    db.session.execute('INSERT INTO telegramGroupUser VALUES ({},{})'.format(groupId, userId))


def checkGroupUser(groupId, userId):
    return list(
        db.session.execute('SELECT *  from telegramGroupUser where groupId ={} and  userId={}'.format(groupId, userId)))

def checkGroupUser(groupId, userId):
    return list(
        db.session.execute('SELECT *  from telegramGroupUser where groupId ={} and  userId={}'.format(groupId, userId)))

def getAllGroup():
    groups=telegramGroup.query.filter_by().all()
    return groups

def getAllUserByGroup(groupId):
    sql='SELECT userId  from telegramGroupUser where groupId ={} '.format(groupId)
    userResults=list(db.session.execute(sql))
    users=[]
    for userResult in userResults:
        userId=userResult.userId
        user=telegramUser.query.filter_by(id=userId).first()
        users.append(user)
    return users
def getUsertype(groupId):
    sql = 'SELECT telegramUser.label as label from telegramGroupUser,telegramUser where telegramGroupUser.groupId ={} and telegramUser.id=telegramGroupUser.userId'.format(groupId)
    userResults = list(db.session.execute(sql))
    res=list(map(lambda x:x[0],userResults))
    return res
def getGroupById(userId):
    user=telegramGroup.query.filter_by(id=userId).first()
    return user
def getAllSIMGroupInfoByUser(userId):
    sql = 'SELECT * from simgroup where userId={}'.format(userId)
    res = list(db.session.execute(sql))
    if len(res)!=0:
        index=res[0][0]
    else:
        index=1
    sql = 'SELECT * from simgroup where simgroup.index={}'.format(index)
    res = list(db.session.execute(sql))
    return res
def getAllSIMGroupInfo():
    sql = 'SELECT * from simgroup '
    res = list(db.session.execute(sql))
    return res
def getAllUserById():
    users = telegramUser.query.filter_by().all()
    return users[1:]
def getAllUserId():
    users = telegramUser.query.filter_by().all()
    ids=[]
    i=0
    for user in users:
        ids.append(user.id)
        i+=1
        if i >=50:
            break
    print("ids",ids)
    return ids
def getUserById(userId):
    user=telegramUser.query.filter_by(id=userId).first()
    return user


