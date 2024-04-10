import requests
import json

from model.telegramDB import getAllSIMGroupInfo, getAllSIMGroupInfoByUser


def getGraphDataById(nodeId):
    print("nodeID")
    cypher = "match (n1)-[p]-(n2) where id(n1)={} return n1,p,n2".format(nodeId)
    return getGraphData(cypher)
def getALLGraphData():
    cypher = "match (n1)-[p]-(n2)  return n1,p,n2"
    return getGraphData(cypher)
def getDataByUerID(userId):
    cypher = "match (n1)-[p]-(n2) WHERE n1.name CONTAINS '{}' return n1,p,n2".format(userId)
    return getGraphData(cypher)
def getDataByUerIDAndType(userId,nodeType):
    cypher = "match (n1)-[p]-(n2:{}) WHERE n1.name CONTAINS '{}'  return n1,p,n2".format(nodeType,userId)
    return getGraphData(cypher)
def getGraphData(cypher):
    url = "http://120.53.228.113:7474/db/data/transaction/commit"
    payload = json.dumps({
        "statements": [
            {
                "statement": cypher,
                "resultDataContents": [
                    "graph"
                ]
            }
        ]
    })
    headers = {
        'Accept': 'application/json;charset=UTF-8',
        'Authorization': 'Basic bmVvNGo6ZXJvY2hOZW80ag==',
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    neo4jData = json.loads(response.text)["results"][0]["data"]
    nodes = []
    links = []
    for data in neo4jData:
        print(data["graph"])
        for node in data["graph"]["nodes"]:
            if node not in nodes:
                nodes.append(node)
        for relationship in data["graph"]["relationships"]:
            relationship["source"] = relationship["startNode"]
            relationship["target"] = relationship["endNode"]
            relationship["linknum"] = 8
            links.append(relationship)
    print(len(nodes), len(links))
    print(nodes)
    print(links)
    graphData = {"nodes": nodes, "links": links}
    return graphData
def createNode(nodeId,nodeName,nodeType):
    node= {
            "id": str(nodeId),
            "labels": [
                nodeType
            ],
            "properties": {
                "name": nodeName,
                "source": "Telegram",
                "type": "SIM"
            }
        }
    return node
def createLink(linkId,source,target,type):
    linkDict = {
        "id": linkId,
        "type": type,
        "startNode": source,
        "endNode": target,
        "properties": {},
        "source": source,
        "target": target,
        "linknum": 5
    }
    return linkDict
def getGroupAnalyseGraphDataByUser(userId):
    allrecord = getAllSIMGroupInfoByUser(userId)
    res = {"nodes": [], "links": []}
    currentGroupId = 0
    currentGroupIndex = -1
    currentId = 0
    Id = 0
    currentLinkId = 0
    groupId = -1
    for record in allrecord:
        if currentGroupIndex == record[0]:
            res["nodes"].append(createNode(Id, record[1], "Person"))
            nodeId = Id
            Id += 1
            res["links"].append(createLink(Id, groupId, nodeId, "ASSOCIATE"))
            Id += 1
        else:
            currentGroupIndex = record[0]
            res["nodes"].append(createNode(Id,"团伙"+str(record[0]), "SIMGROUP"))
            groupId = Id
            Id += 1
            res["nodes"].append(createNode(Id, record[1], "Person"))
            nodeId = Id
            Id += 1
            res["links"].append(createLink(Id, groupId, nodeId, "ASSOCIATE"))
            Id += 1
    return res
def getGroupAnalyseGraphData():
    allrecord = getAllSIMGroupInfo()
    res={"nodes": [],"links": []}
    currentGroupId = 0
    currentGroupIndex=-1
    currentId=0
    Id=0
    currentLinkId=0
    groupId=-1
    for record in allrecord:
        if currentGroupIndex==record[0]:
            res["nodes"].append(createNode(Id,record[1],"Person"))
            nodeId=Id
            Id+=1
            res["links"].append(createLink(Id,groupId,nodeId,"ASSOCIATE"))
            Id += 1
        else:
            currentGroupIndex=record[0]
            res["nodes"].append(createNode(Id, "团伙"+str(record[0]), "SIMGROUP"))
            groupId = Id
            Id += 1
            res["nodes"].append(createNode(Id, record[1], "Person"))
            nodeId = Id
            Id += 1
            res["links"].append(createLink(Id, groupId, nodeId, "ASSOCIATE"))
            Id += 1
    return res
def getAllSIMGroup():
    res=getAllSIMGroupInfo()
    currentId=1
    resList=[]
    singleDict = {"personList": [],"info":{"phoneNumber": ["180", "170", "155"], "aim": ["联通", "电信"] }}
    for record in res:
        if record[0]==currentId:
            singleDict["personList"].append(record[1])
        else:
            resList.append(singleDict)
            currentId=record[0]
            singleDict = {"personList": [],"info":{ "phoneNumber": ["180", "170", "155"], "aim": ["联通", "电信"]}}
            if currentId==10:
                singleDict = {"personList": [],"info":{ "号段": ["171-170", "162", "155","170","180"], "类型": ["白名单电销卡"],"归属地":["北京","上海","深圳","东莞","重庆","武汉","苏州","合肥","厦门","南京","青岛","廊坊"]}}
            singleDict["personList"].append(record[1])
    return resList
