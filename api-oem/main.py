import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast

#connect to banks multichain node
load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))
bank = next((node for node in nodes if node['name'] == 'oem'), None)
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
        return {"data":"hi"}

#create 0 tradable asset named name dividable by 1
class createAsset(self):
    def post(self):
        data = request.get_json()
        client.issue(client.listaddresses()[0]['address'], 
            {"name":data["name"],
            "open":True},
            0,1
        )
        return {"data":data["name"]}

#path to issue qty more name
class issueMoreAsset(self):
    def post(self):
        data = request.get_json()
        client.issuemore(client.listaddresses()[0]['address'], 
            data["name"],
            data["qty"]
        )
        return {"data":data["name"]}

#create path to refund
class refund(Resource):
    def post(self):
        data = request.get_json()
        pattern = re.compile("(?<=burnaddress': ')[0-9][A-Za-z0-9]+")
        burnAddress = pattern.findall(str(client.getinfo()))[0]
        client.importaddress(burnAddress)
        try:
            client.sendasset(burnAddress,"EUR",data['amount'])
            return {"data":data['amount']}
        except:
            return {"data":"ERROR, not enough funds"}

api.add_resource(helloWorld, '/')
api.add_resource(refund, '/api/v1/refund')

if __name__ == '__main__':
    app.run()

