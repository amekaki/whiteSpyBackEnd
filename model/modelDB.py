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
class commentLog(db.Model):
    __tablename__ = 'commentLog'  # 指定对应数据库表comment
    postID=db.Column(db.Integer,primary_key=True)
    userID=db.Column(db.VARCHAR(20),primary_key=True)
    content=db.Column(db.UnicodeText)
    commentTime=db.Column(db.DateTime(6))

    def __init__(self,postID,userID,content,commentTime):
        self.postID=postID
        self.userID=userID
        self.content=content
        self.commentTime=commentTime

    def __repr__(self):
        return '<commentLog %r>' % self.content

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        item['commentTime']=item['commentTime'].strftime("%Y-%m-%d-%H")
        return item

