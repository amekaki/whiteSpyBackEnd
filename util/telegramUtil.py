from telethon import TelegramClient
import asyncio
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
# Use your own values from my.telegram.org
api_id=2618121  # Use your own values from my.telegram.org,
api_hash='3de6a9e4d1ab7f17f9619e11b4a1a468'  # 这里填写在第四步中申请的api_id和api_hash

async def work(client):
    async with client:
        me = await client.get_me()
        print('Working with', me.first_name)
async def sendMessage(client,target,message):
    async with client:
        await client.send_message(target, message)
async def getGroup(phoneNumber):
    print(phoneNumber)
    session="util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await work(TelegramClient(session, api_id, api_hash,proxy=("socks5", '127.0.0.1', 7891)))

async def sendToUser(phoneNumber,target,message):
    print(phoneNumber,target,message)
    session="util/telethonSession/getInfoSession/{}".format(phoneNumber)
    await sendMessage(TelegramClient(session, api_id, api_hash,proxy=("socks5", '127.0.0.1', 7891)),target,message)
async def getGroupInfo(phoneNumber):
    session = "util/telethonSession/getInfoSession/{}".format(phoneNumber)
    client=TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7891))
    async with client:
        me = await client.get_me()
        my_chat = await client.get_entity('@sim114')
        my_fr = await client.get_entity('@Gzh123')
        xx()
        path = await client.download_profile_photo('@Gzh123')
        print(path)
        print("chat",my_chat)
        print("user",my_fr)
        return path
