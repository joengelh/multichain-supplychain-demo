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

#create root path
class helloWorld(Resource):
    def get(self):
        return {'data':'hi'}

#create path to create stream, requires name
class createStream(Resource):
    def post(self):
        data = request.get_json()
        try:
            client.create("stream",data["name"],False)
            return {'data':"Stream created!"}
        except:
            return {'data':"Stream already exists!"}

#create path to publish to stream, requires name, key, data-json
#postman example: {"name":"package001","key":"sensor","data-json":
#{"json":{"temperatur":40,"humidity":400,"maxG":0.1,
#"location":"N12314E123123"}}}
class initiate(Resource):
    def post(self):
        data = request.get_json()
        client.publish(data["name"],data["key"],data["data-json"])
        return {'data':data["data-json"]}

class terminate(Resource):
    def post(self):
        data = request.get_json()
        client.publish(data["name"],data["key"],data["data-json"])
        return {'data':data["data-json"]}

api.add_resource(helloWorld, '/')
api.add_resource(createStream, '/api/v1/createStream')
api.add_resource(publish, '/api/v1/publish')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)




