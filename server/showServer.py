import requests
import json


def getGraphDataById(nodeId):
    url = "http://123.56.242.44:7474/db/data/transaction/commit"
    cypher = "match (n1)-[p]-(n2) where id(n1)={} return n1,p,n2".format(nodeId)
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
