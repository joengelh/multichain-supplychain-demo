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
    #create EUR asset class with 0 balance, issuable and devidable by 0.01 
    client.issue(client.listaddresses()[0]['address'], {"name":"EUR","open":True},0,0.01)
except:
    pass

app = Flask(__name__)
api = Api(app)

class helloWorld(Resource):
    def get(self):
        return {"data":"hi"}

class balance(Resource):
    def post(self):
        data = request.get_json()
        client.importaddress(data['account'])
        return {"data":client.getaddressbalances(data['account'])}


api.add_resource(helloWorld, '/')
api.add_resource(balance, '/api/v1/balance')

if __name__ == '__main__':
    app.run()


#for server in tradableServers:
    #issue asset class for every server, quantitiy zero, devisible by 1
#    client.issue(client.listaddresses()[0]['address'], {"name":server,"open":True},0,1)
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"dellserver",600,1)
#client.sendasset(burnAddress,"hpeServer",300)
#