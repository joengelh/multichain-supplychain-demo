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

#create root path
class helloWorld(Resource):
    def get(self):
        return {'data':'hi'}

#create new iot device writing to stream,
#creating stream if not already present
class create(Resource):
    def post(self):
        data = request.get_json()
        iot.create(data["name"])
        return {'data':data["name"]}

#destroy iot device thus not writing to stream furtherly
class destroy(Resource):
    def post(self):
        data = request.get_json()
        iot.destroy(data["name"])
        return {'data':data["name"]}

#list active iot devices writing to streams
class listAll(Resource):
    def get(self):
        return {'data':iot.listAll()}

api.add_resource(helloWorld, '/')
api.add_resource(create, '/api/v1/create')
api.add_resource(destroy, '/api/v1/destroy')
api.add_resource(listAll, '/api/v1/listAll')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)




