from model.userDB import getUserByPhoneNumber


def getUserInfo(phonenumber):
    user=getUserByPhoneNumber(phonenumber)
    return user.to_json()