import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast

import virtualIotDevice

#connect to banks multichain node
load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))
bank = next((node for node in nodes if node['name'] == 'iot'), None)
client = c = mcrpc.RpcClient(
        bank['ip'], 
        bank['port'], 
        bank['user'],
        bank['password']
    )

#initiate falsk app
app = Flask(__name__)
api = Api(app)

#initiate virtualIotDevice
iot = virtualIotDevice.iot()

#activate root path
class helloWorld(Resource):
    def get(self):
        return {'data':'hi'}

#activate new iot device writing to stream,
#creating stream if not already present
class activate(Resource):
    def post(self):
        data = request.get_json()
        iot.activate(data["name"])
        return {'data':data["name"]}

#deactivate iot device thus not writing to stream furtherly
class deactivate(Resource):
    def post(self):
        data = request.get_json()
        iot.deactivate(data["name"])
        return {'data':data["name"]}

#list active iot devices writing to streams
class listAll(Resource):
    def get(self):
        return {'data':iot.listAll()}

api.add_resource(helloWorld, '/')
api.add_resource(activate, '/api/v1/activate')
api.add_resource(deactivate, '/api/v1/deactivate')
api.add_resource(listAll, '/api/v1/listAll')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)




