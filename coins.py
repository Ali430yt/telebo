import time,os
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("@QQQQQQ2")
ch = str(input("Enter Usernam: "))
api_id = '2192036'
api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
client = TelegramClient('session', api_id, api_hash)
client.start()
while True:
    try:
        client.send_message(ch ,"كلمات")
        time.sleep(1)
        mssag = client.get_messages(ch, limit=1)
        text1 = str(mssag[0].message).split("(")[1]
        text2 = str(text1.split(")")[0])
        text = str(text2.strip())
        client.send_message(ch ,text)
        time.sleep(1)
        getcoin = client.get_messages(ch, limit=1)
        coin = str(getcoin[0].message).split("💸فلوسك:")
        client.send_message(ch ,"مضاربه 500")
        client.send_message(ch ,"بخشيش")
        client.send_message(ch ,"راتب")
        client.send_message(ch ,"حظ 500")
        print(coin[1])
        print("@QQQQQQ2")
    except:
        pass