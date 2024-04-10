from telethon import TelegramClient
import asyncio
from telethon import functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.custom.chatgetter import ChatGetter
from telethon import utils
# Use your own values from my.telegram.org
# from model.telegramDB import checkUser
from model.telegramDB import checkUser, checkGroup, checkGroupById

api_id = 2618121  # Use your own values from my.telegram.org,
api_hash = '3de6a9e4d1ab7f17f9619e11b4a1a468'  # 这里填写在第四步中申请的api_id和api_hash

async def work(client):
    async with client:
        me = await client.get_me()
        print('Working with', me.first_name)
async def startChat(client,id):
    async with client:
        me = await client.get_me()
    # await client.send_message(PeerUser(id), 'Hello, myself!')

async def sendMessage(phoneNumber, target, message):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        await client.send_message(target, message)
async def sendMessageToUserList(phoneNumber, targetList, message):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        for target in targetList:
            await client.send_message(target, message)
async def getGroup(phoneNumber):
    print(phoneNumber)
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await work(TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808)))

async def sendToUser(phoneNumber, target, message):
    print(phoneNumber, target, message)
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await sendMessage(TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808)), target, message)

async def getGroupUser(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        my_chat = await client.get_entity(groupName)
        users = await client.get_participants(my_chat)
        userInfo = []
        # for user in users:
        for i in range(len(userInfo)):
            user=users[i]
            checkUserexist=checkUser(user.id)
            if checkUserexist:
                path='static/img/groupImg/2.jpg'
            else:
                path = await client.download_profile_photo(user.id,
                                                           file='static\\img\\userImg\\{}.jpg'.format(user.id))
                if path is None:
                    path = 'static/img/groupImg/2.jpg'
                else:
                    path = path.replace("\\", "/")
            userInfo.append({"userInfo":user,"imgPath":path})
            print(user)
            # print(user)
        print(userInfo[0]["userInfo"])
        return userInfo
async def getGroupInfoQuery(phoneNumber, search):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        result = await client(functions.contacts.SearchRequest(
            q=search,
            limit=100
        ))
        groupListE=result.chats
        groupList=[]

        print(result.chats,type(result.chats))
        for group in groupListE:
            print(group)
            checkg = checkGroupById(group.id)
            if checkg:
                print("已存在")
                path=checkg
            else:
                path = 'static/img/groupImg/{}.jpg'.format(group.id)
                print(group.photo,type(group.photo))
                path = await client.download_profile_photo(group.id,file='static\\img\\groupImg\\')
                if path is not None:
                    path=path.replace('\\','/')
                else:
                    path='static/img/groupImg/2.jpg'
                print("path", path)
            groupList.append({"group":group,"path":path})
        return groupList
async def getGroupListInfo(phoneNumber, groupNameList):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        groupList=[]
        for groupName in groupNameList:
            my_chat = await client.get_entity(groupName)
            print("chat",my_chat)
            path = await client.download_profile_photo(groupName,file='static\\img\\groupImg\\')
            if path is not None:
                path=path.replace('\\','/')
            else:
                path='static/img/groupImg/2.jpg'
            print("path", path)
            groupList.append({"group":my_chat,"path":path})
        return groupList
async def getGourpConcat(phoneNumber,search):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        result = await client(functions.contacts.SearchRequest(
            q=search,
            limit=100
        ))
        print(result.stringify())
        return "result.stringify()"
async def getGroupInfo(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        me = await client.get_me()
        my_chat = await client.get_entity(groupName)
        print("chat",my_chat)
        path = await client.download_profile_photo(groupName,file='static\\img\\groupImg\\{}.jpg'.format(groupName))
        if path is not None:
            path=path.replace('\\','/')
        else:
            path='static/img/groupImg/2.jpg'
        print("path", path)
        return my_chat,path

async def getGroupChattingRecords(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        # chats = await client.get_messages(groupName,1000, from_user='@Gzh123')
        chats = await client.get_messages(groupName,10)
        print("成功获取")
        chatList = []
        userDict= {}
        print("chats",chats,chats[0].from_id)
        for chat in chats:
            if(chat.from_id):
                userId=str(chat.from_id.user_id)
                if userId in userDict:
                    pass
                else:
                    sendUser = await client.get_entity(chat.from_id)
                    path = await client.download_profile_photo(sendUser.id, file='static\\img\\userImg\\{}.jpg'.format(sendUser.id))
                    if path is None:
                        path = 'static/img/groupImg/2.jpg'
                    else:
                        path=path.replace("\\","/")
                first_name=sendUser.first_name
            else:
                userId=0
                path = 'static/img/groupImg/2.jpg'
                first_name="channel"
            path='http://localhost:5000/download?filepath='+path
            userDict[userId]={'userName':first_name,'avatarPath':path}
            chatrecord = {"message": chat.message, "sender":userDict[userId],"sendTime":chat.date.strftime('%Y-%m-%d %H:%M:%S')}
            chatList.append(chatrecord)
        return chatList
async def getUserInfo(phoneNumber,username):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        sendUser = await client.get_entity(username)
        print(sendUser)
        return sendUser
async def getGroupChatRecords(phoneNumber, groupName):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 10808))
    async with client:
        # chats = await client.get_messages(groupName,1000, from_user='@Gzh123')
        chats = await client.get_messages(groupName,10)
        for chat in chats:
            print(chat)
        # print("成功获取")
        # chatList = []
        # userDict= {}
        # print("chats",chats,chats[0].from_id)
        # for chat in chats:
        #     userId=str(chat.from_id.user_id)
        #     if userId in userDict:
        #         pass
        #     else:
        #         sendUser = await client.get_entity(chat.from_id)
        #         path = await client.download_profile_photo(sendUser.id, file='static\\img\\userImg\\{}.jpg'.format(sendUser.id))
        #         if path is None:
        #             path = 'static/img/groupImg/2.jpg'
        #         else:
        #             path=path.replace("\\","/")
        #         path='http://localhost:5000/download?filepath='+path
        #         userDict[userId]={'userName':sendUser.first_name,'avatarPath':path}
        #     chatrecord = {"message": chat.message, "sender":userDict[userId],"sendTime":chat.date.strftime('%Y-%m-%d %H:%M:%S')}
        #     chatList.append(chatrecord)
        # print(chatList)
        return 1
if __name__ == '__main__':
    asyncio.run(getUserInfo("+8618956778851", "@eroch"))
    # asyncio.run(getGourpConcat("+8618956778851","SIM6"))
    # asyncio.run(sendMessageToUserList("+8618956778851",[1663335744,1311000018,1663335744],"出卡吗"))
