from flask import Blueprint, request
import json
from server.showServer import getGraphDataById, getALLGraphData, getDataByUerID, getDataByUerIDAndType, getAllSIMGroup, \
    getGroupAnalyseGraphData, getGroupAnalyseGraphDataByUser

show = Blueprint("show", __name__)


@show.route('/getGraphDataByNodeId', methods=['post'])
def ggdxxt():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    nodeId = int(req['nodeId'])
    graphData = getGraphDataById(nodeId)
    return json.dumps(graphData)


@show.route('/getGraphDataByUserId', methods=['post'])
def ggdxt():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    userId = req['userId']
    graphData = getDataByUerID(userId)
    return json.dumps(graphData)


@show.route('/getGraphDataByNodeType', methods=['post'])
def sss():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    userId = req['userId']
    nodeType = req['nodeType']
    graphData = getDataByUerIDAndType(userId, nodeType)
    return json.dumps(graphData)

@show.route('/getAllGraphData', methods=['post'])
def gaagdt():
    graphData = getALLGraphData()
    return json.dumps(graphData)


@show.route('/getGroupStatistic', methods=['post'])
def ggstistic():
    data = {"groupNumber": 32, "personNumber": 438}
    return json.dumps(data)

@show.route('/getGroupListInfo', methods=['post'])
def ggsinfo():
    data=getAllSIMGroup()
    # data = [{"personList": [1821624503, 1821624503], "phoneNumber": ["180", "170", "155"], "aim": ["联通", "电信"]},{"personList": ["111", "222"], "phoneNumber": ["180", "170", "155"], "aim": ["联通", "电信"]},{"personList": ["111", "222"], "phoneNumber": ["180", "170", "155"], "aim": ["联通", "电信"]}]
    return json.dumps(data)
@show.route('/getGroupAnalyseGraphByUser', methods=['post'])
def gggxxwwdc():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    userId = req['userId']
    graphData = getGroupAnalyseGraphDataByUser(userId)
    return json.dumps(graphData)

@show.route('/getGroupAnalyseGraph', methods=['post'])
def gggraphc():
    graphData = getGroupAnalyseGraphData()
    return json.dumps(graphData)
