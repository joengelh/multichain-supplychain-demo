import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
import sys

import virtualIotDevice

#get port and name from arguments
print("Give name of client as first, port as second argument like python3 api-shareHolder/main.py oem 5003")
NAME = sys.argv[1]
PORT = sys.argv[2]

#connect to banks multichain node
load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))
bank = next((node for node in nodes if node['name'] == NAME), None)
client = c = mcrpc.RpcClient(
        bank['ip'], 
        bank['port'], 
        bank['user'],
        bank['password']
    )

#initiate virtualIotDevice
iot = virtualIotDevice.iot()

#initiate falsk app
app = Flask(__name__)
api = Api(app)

#create root path
class helloWorld(Resource):
    def get(self):
        return {'data':'hi'}

#create path to check balance, requires asset
class balance(Resource):
    def get(self):
        data = request.get_json()
        balances = client.getaddressbalances(client.listaddresses()[0]['address'])
        if balances != 0:
            balanceAsset = next((item for item in balances if item['name'] == data['name']), None)
            return {'data':balanceAsset['qty']}
        else: 
            return {'data':0}

#create path to check balance
class inventory(Resource):
    def get(self):
        result = client.getaddressbalances(client.listaddresses()[0]['address'])
        return {'data':result}

#create path to get address
class ownAddress(Resource):
    def get(self):
        return {'data':client.listaddresses()[0]['address']}

#create path to add amount funds to address, issuing if required
class issue(Resource):
    def post(self):
        data = request.get_json()
        try:
            client.issue(client.listaddresses()[0]['address'], 
                {'name':data['name'],'open':True},0,1)
        except:
            pass
        result = client.issuemore(client.listaddresses()[0]['address'],
            data['name'],data['amount'])
        return {'data':result}

#create path to send
class send(Resource):
    def post(self):
        data = request.get_json()
        result = client.sendasset(data['address'],data['name'],data['amount'])
        return {'data':result}

#create path to create exchange requireing asset and price
class atomicExchange(Resource):
    def post(self):
        data = request.get_json()
        lock = client.preparelockunspent({data["name"]:data["amount"]},False)
        result = client.createrawexchange(lock["txid"],
            lock["vout"],{data["barter"]:data["price"]})
        return {'data':result}

#create path to decode exchange
class reviewExchange(Resource):
    def get(self):
        data = request.get_json()
        result = client.decoderawexchange(data["proposal"])
        return {'data':result}

#create path to accept exchange
class acceptExchange(Resource):
    def post(self):
        data = request.get_json()
        proposal = client.decoderawexchange(data["proposal"])
        lock = client.preparelockunspent(
            {proposal["ask"]["assets"][0]["name"]:proposal["ask"]["assets"][0]["qty"]},False)
        result = client.completerawexchange(data["proposal"],lock["txid"],0,
            {proposal["offer"]["assets"][0]["name"]:proposal["offer"]["assets"][0]["qty"]})
        return {'data':result}

#create path to withdraw from exchange
class withdrawExchange(Resource):
    def post(self):
        data = request.get_json()
        result = client.disablerawtransaction(data["proposal"])
        return {'data':result}

#create path to list wallets transactions
class history(Resource):
    def get(self):
        return {'data':client.listwallettransactions()}

#activate new iot device writing to stream,
#creating stream if not already present
class activate(Resource):
    def post(self):
        data = request.get_json()
        return {'data':iot.activate(data["name"])}

#deactivate iot device thus not writing to stream furtherly
class deactivate(Resource):
    def post(self):
        data = request.get_json()
        return {'data':iot.deactivate(data["name"])}

#list active iot devices writing to streams
class listActive(Resource):
    def get(self):
        return {'data':iot.listActive()}

#list items written by IoT Device
class listItems(Resource):
    def get(self):
        data = request.get_json()
        return {'data':iot.listItems(data["name"])}

api.add_resource(helloWorld, '/')
api.add_resource(ownAddress, '/api/v1/ownAddress')
api.add_resource(balance, '/api/v1/balance')
api.add_resource(inventory, '/api/v1/inventory')
api.add_resource(issue, '/api/v1/issue')
api.add_resource(send, '/api/v1/send')
api.add_resource(atomicExchange, '/api/v1/atomicExchange')
api.add_resource(reviewExchange, '/api/v1/reviewExchange')
api.add_resource(acceptExchange, '/api/v1/acceptExchange')
api.add_resource(withdrawExchange, '/api/v1/withdrawExchange')
api.add_resource(history, '/api/v1/history')
api.add_resource(activate, '/api/v1/activate')
api.add_resource(deactivate, '/api/v1/deactivate')
api.add_resource(listActive, '/api/v1/listActive')
api.add_resource(listItems, '/api/v1/listItems')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))

