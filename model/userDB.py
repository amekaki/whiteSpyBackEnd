from model.modelDB import *
def getUserByPhoneNumberAndPassword(phoneNumber,password):
    userResult=User.query.filter_by(phoneNumber=phoneNumber,password=password).first()
    return userResult

def getUserByPhoneNumber(phoneNumber):
    userResult=User.query.filter_by(phoneNumber=phoneNumber).first()
    return userResult

def insertUser(phoneNumber,password,userName):
    user=User(userName,password,phoneNumber)
    db.session.add(user)
    db.session.commit()