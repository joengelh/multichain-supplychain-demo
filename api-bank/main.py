import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

#connect to banks multichain node
load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))
bank = next((node for node in nodes if node['name'] == 'bank'), None)
client = c = mcrpc.RpcClient(
        bank['ip'], 
        bank['port'], 
        bank['user'],
        bank['password']
    )
try:
    #create EUR asset class with 100 mil € balance, issuable and devidable by 0.01 
    client.issue(client.listaddresses()[0]['address'], {"name":"EUR","open":True},100000000,0.01)
except:
    pass

#initiate falsk app
app = Flask(__name__)
api = Api(app)

#create root path
class helloWorld(Resource):
    def get(self):
        return {"data":"hi"}

#create path to check balance
class balance(Resource):
    def post(self):
        data = request.get_json()
        client.importaddress(data['account'])
        balances = client.getaddressbalances(data['account'])
        balanceEur = next((item for item in balances if item["name"] == "EUR"), None)
        return {"data":balanceEur}

#create path to get bank address
class ownAddress(Resource):
    def get(self):
        return {"data":client.listaddresses()[0]['address']}

#create path to get nrun address
class burnAddress(Resource):
    def get(self):
        pattern = re.compile("(?<=burnaddress': ')[0-9][A-Za-z0-9]+")
        burnAddress = pattern.findall(str(client.getinfo()))[0]
        return {"data":burnAddress}


#create path to add amount funds to address
class fund(Resource):
    def post(self):
        data = request.get_json()
        client.issuemore(data['account'],"EUR",data['amount'])
        client.importaddress(data['account'])
        return {"data":client.getaddressbalances(data['account'])}

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
api.add_resource(ownAddress, '/api/v1/ownAddress')
api.add_resource(burnAddress, '/api/v1/burnAddress')
api.add_resource(balance, '/api/v1/balance')
api.add_resource(fund, '/api/v1/fund')
api.add_resource(refund, '/api/v1/refund')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
