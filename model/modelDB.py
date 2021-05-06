from model import db

class User(db.Model):
    __tablename__ = 'user'  # 指定对应数据库表user
    userName = db.Column(db.VARCHAR(20))
    password = db.Column(db.VARCHAR(20))
    phoneNumber=db.Column(db.VARCHAR(20),primary_key=True)
    headPortrait=db.Column(db.VARCHAR(100))
    # userID=db.Column(db.Integer)
    # TODO 添加邮箱、手机号属性
    def __init__(self,userName,password,phoneNumber,headPortrait):
        self.userName=userName
        self.password=password
        self.phoneNumber=phoneNumber
        self.headPortrait=headPortrait

    def __repr__(self):
        return '<User %r>' % self.userName

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['headPortrait'] = 'http://localhost:5000/download?filepath=' + item['headPortrait']
        return item
class Post(db.Model):
    __tablename__ = 'post'  # 指定对应数据库表post
    author = db.Column(db.VARCHAR(20))
    cover = db.Column(db.VARCHAR(100))
    type = db.Column(db.VARCHAR(20))
    location=db.Column(db.VARCHAR(20))
    content=db.Column(db.UnicodeText)
    postID=db.Column(db.INT,unique=True,primary_key=True)
    modifiedTime=db.Column(db.DateTime(6))
    header=db.Column(db.VARCHAR(100))

    def __init__(self,author,content,location,type,cover,postID,modifiedTime,header):
        self.author=author
        self.content=content
        self.location=location
        self.type=type
        self.cover=cover
        self.postID=postID
        self.modifiedTime=modifiedTime
        self.header=header

    def __repr__(self):
        return '<Post %r>' % self.header

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['modifiedTime']=item['modifiedTime'].strftime("%Y-%m-%d-%H")
        item['cover']='http://localhost:5000/download?filepath='+item['cover']
        return item

class starLog(db.Model):
    __tablename__ = 'starLog'  # 指定对应数据库表post
    postID=db.Column(db.Integer,primary_key=True)
    userID=db.Column(db.VARCHAR(20),primary_key=True)
    starTime=db.Column(db.DateTime(6))
    def __init__(self,postID,userID,starTime):
        self.postID=postID
        self.userID=userID
        self.starTime=starTime
    def __repr__(self):
        return '<starLog %r>' % self.postID

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['starTime']=item['starTime'].strftime("%Y-%m-%d-%H")
        return item


class telegramGroup(db.Model):
    __tablename__ = 'telegramGroup'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(255))
    photo = db.Column(db.VARCHAR(255))
    username = db.Column(db.VARCHAR(255))
    date = db.Column(db.DateTime(6))

    def __init__(self,id,title,photo,username,date):
        self.id=id
        self.title=title
        self.photo=photo
        self.username=username
        self.date=date


    def __repr__(self):
        return "<teleGramGroup %r>" % self.username

    def to_json(self):
        item=self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['photo'] = 'http://localhost:5000/download?filepath=' + item['photo']
        item['date'] = item['date'].strftime("%Y-%m-%d-%H")
        return item

class telegramUser(db.Model):
    __tablename__ = 'telegramUser'
    __table_args__ = {'mysql_engine' : 'InnoDB', 'mysql_charset' : 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(255))
    last_name = db.Column(db.VARCHAR(255))
    photo = db.Column(db.VARCHAR(255))
    username = db.Column(db.VARCHAR(255))
    phone = db.Column(db.VARCHAR(255))
    label=db.Column(db.VARCHAR(255))

    def __init__(self,id,first_name,last_name,photo,username,phone,label=None):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.photo=photo
        self.username=username
        self.phone=phone
        self.label=label


    def __repr__(self):
        return "<telegramUser %r>" % self.id

    def to_json(self):
        item=self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['photo'] = 'http://localhost:5000/download?filepath=' + item['photo']
        return item

class Message(db.Model):
    __table_name__='message'
    msgId = db.Column(db.Integer, primary_key=True)
    isSend=db.Column(db.Integer)
    senderId = db.Column(db.Integer)
    content= db.Column(db.VARCHAR(1000))
    createTime = db.Column(db.DateTime(6))
    intent=db.Column(db.VARCHAR(255))

    def __init__(self,msgId,isSend,senderId,content,createTime,intent):
        self.senderId=senderId
        self.msgId=msgId
        self.isSend=isSend
        self.content=content
        self.intent=intent
        self.createTime=createTime
    def __repr__(self):
        return "<Message %r>" % self.msgId

    def to_json(self):
        item=self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['createTime'] = item['createTime'].strftime("%Y-%m-%d-%H")
        return item

