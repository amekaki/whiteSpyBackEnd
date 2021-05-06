from telethon import TelegramClient
import asyncio
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.custom.chatgetter import ChatGetter
from telethon import utils
# Use your own values from my.telegram.org
from model.telegramDB import checkUser

api_id = 2618121  # Use your own values from my.telegram.org,
api_hash = '3de6a9e4d1ab7f17f9619e11b4a1a468'  # 这里填写在第四步中申请的api_id和api_hash

async def work(client):
    async with client:
        me = await client.get_me()
        print('Working with', me.first_name)

async def sendMessage(client, target, message):
    async with client:
        await client.send_message(target, message)

async def getGroup(phoneNumber):
    print(phoneNumber)
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await work(TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891)))

async def sendToUser(phoneNumber, target, message):
    print(phoneNumber, target, message)
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await sendMessage(TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891)), target, message)

async def getGroupUser(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891))
    async with client:
        my_chat = await client.get_entity(groupName)
        users = await client.get_participants(my_chat)
        userInfo = []
        # for user in users:
        for i in range(5):
            user=users[i]
            checkUserexist=checkUser(user.id)
            if checkUserexist:
                path='static/img/headPortrait/2.jpg'
            else:
                path = await client.download_profile_photo(user.id,
                                                           file='static\\img\\userImg\\{}.jpg'.format(user.id))
                if path is None:
                    path = 'static/img/headPortrait/2.jpg'
                else:
                    path = path.replace("\\", "/")
            userInfo.append({"userInfo":user,"imgPath":path})
        print(userInfo[0]["userInfo"])
        return userInfo
async def getGroupListInfo(phoneNumber, groupNameList):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891))
    async with client:
        groupList=[]
        for groupName in groupNameList:
            my_chat = await client.get_entity(groupName)
            print("chat",my_chat)
            path = await client.download_profile_photo(groupName,file='static\\img\\groupImg\\')
            if path is not None:
                path=path.replace('\\','/')
            else:
                path='static/img/headPortrait/2.jpg'
            print("path", path)
            groupList.append({"group":my_chat,"path":path})
        return groupList
async def getGroupInfo(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891))
    async with client:
        me = await client.get_me()
        my_chat = await client.get_entity(groupName)
        print("chat",my_chat)
        path = await client.download_profile_photo(groupName,file='static\\img\\groupImg\\{}.jpg'.format(groupName))
        if path is not None:
            path=path.replace('\\','/')
        else:
            path='static/img/headPortrait/2.jpg'
        print("path", path)
        return my_chat,path

async def getGroupChattingRecords(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891))
    async with client:
        # chats = await client.get_messages(groupName,1000, from_user='@Gzh123')
        chats = await client.get_messages(groupName,5)
        print("成功获取")
        chatList = []
        userDict= {}
        print("chats",chats,chats[0].from_id)
        for chat in chats:
            userId=str(chat.from_id.user_id)
            if userId in userDict:
                pass
            else:
                sendUser = await client.get_entity(chat.from_id)
                path = await client.download_profile_photo(sendUser.id, file='static\\img\\userImg\\{}.jpg'.format(sendUser.id))
                if path is None:
                    path = 'static/img/headPortrait/2.jpg'
                else:
                    path=path.replace("\\","/")
                path='http://localhost:5000/download?filepath='+path
                userDict[userId]={'userName':sendUser.first_name,'avatarPath':path}
            chatrecord = {"message": chat.message, "sender":userDict[userId],"sendTime":chat.date.strftime('%Y-%m-%d %H:%M:%S')}
            chatList.append(chatrecord)
        return chatList

# if __name__ == '__main__':
#     asyncio.run(getGroupInfo("+8618956778851","@dajianwangzhan"))
