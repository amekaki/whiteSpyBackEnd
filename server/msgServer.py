import json

from model.messageDB import getMsgLogById


def getMessageByUserId(userId):
    results=getMsgLogById(userId)
    messages=[]
    for result in results:
        if result.isSend==0:
            print(result.content)
            messageJson=json.loads(result.content)
            content=messageJson['text']
            entities=messageJson['entities']
            print(content,entities)
            contentList=[]
            offset = 0
            length=len(content)
            for entity in entities:
                start=entity["start"]
                end=entity["end"]
                name=entity["entity"]
                print(start,end,name)
                if start==offset:
                    text=content[start:end]
                    contentDict={"isEntity":1,"text":text,"entityName":name}
                    contentList.append(contentDict)
                    offset=end
                else:
                    text = content[offset:start]
                    contentDict = {"isEntity": 0, "text": text}
                    contentList.append(contentDict)
                    text = content[start:end]
                    contentDict = {"isEntity": 1, "text": text, "entityName": name}
                    contentList.append(contentDict)
                    offset = end
            print(offset,length-1)
            if offset!=(length-1):
                text = content[offset:]
                contentDict = {"isEntity": 0, "text": text}
                contentList.append(contentDict)
            print("msgList",contentList)
        else:
            contentDict = {"isEntity": 0, "text": result.content}
            contentList=[contentDict]
        result.content=contentList
        messages.append(result)
    return list(map(lambda x:x.to_json(),messages))