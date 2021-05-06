from flask import Blueprint, request
import json
from server.showServer import getGraphDataById

show=Blueprint("show", __name__)

@show.route('/getGraphDataByNodeId',methods=['post'])
def ggdt():
    req = json.loads(request.get_data(as_text=True))
    print("req", req)
    nodeId = int(req['nodeId'])
    graphData=getGraphDataById(nodeId)
    return json.dumps(graphData)