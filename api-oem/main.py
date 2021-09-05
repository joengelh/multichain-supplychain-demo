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
bank = next((node for node in nodes if node['name'] == 'customer'), None)
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

#create path to check balance, requires asset
class balance(Resource):
    def get(self):
        data = request.get_json()
        balances = client.getaddressbalances(client.listaddresses()[0]['address'])
        if balances != 0:
            balanceAsset = next((item for item in balances if item["name"] == data["asset"]), None)
            return {"data":balanceAsset["qty"]}
        else: 
            return {"data":balances}

#create path to check balance
class inventory(Resource):
    def get(self):
        data = request.get_json()
        balances = client.getaddressbalances(client.listaddresses()[0]['address'])
        return {"data":balances}

#create path to get address
class ownAddress(Resource):
    def get(self):
        return {"data":client.listaddresses()[0]['address']}

#create path to issue assets
class issue(Resource):
    def post(self):
        data = request.get_json()
        try:
            client.issue(client.listaddresses()[0]['address'], 
                {"name":data["asset"],"open":True},0,1)
            return {"data":"Asset issued!"}
        except:
            return {"data":"Asset already issued!"}

#create path to add amount funds to address
class issueMore(Resource):
    def post(self):
        data = request.get_json()
        client.issuemore(client.listaddresses()[0]['address'],
            data["asset"],data['amount'])
        return {"data":data["amount"]}

#create path to refund
class send(Resource):
    def post(self):
        data = request.get_json()
        client.sendasset(data["address"],data["asset"],data['amount'])
        return {"data":data['amount']}
        
api.add_resource(helloWorld, '/')
api.add_resource(ownAddress, '/api/v1/ownAddress')
api.add_resource(balance, '/api/v1/balance')
api.add_resource(inventory, '/api/v1/inventory')
api.add_resource(issue, '/api/v1/issue')
api.add_resource(issueMore, '/api/v1/issueMore')
api.add_resource(send, '/api/v1/send')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)




