import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

#import classes from ./ folder
import multichainAccess

load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))
bank = next((node for node in nodes if node['name'] == 'bank'), None)

app = Flask(__name__)
api = Api(app)

mc = multichainAccess.blockchainAccess()

class helloWorld(Resource):
    def get(self):
        return {"data":"hi"}

class fund(Resource):
    pass

class refund(Resource):
    pass

api.add_resource(helloWorld, '/')
api.add_resource(mc.fund, '/api/v1/fund')
api.add_resource(mc.refund, '/api/v1/refund')

if __name__ == '__main__':
    app.run()

#for server in tradableServers:
    #issue asset class for every server, quantitiy zero, devisible by 1
#    client.issue(client.listaddresses()[0]['address'], {"name":server,"open":True},0,1)
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"dellserver",600,1)
#client.sendasset(burnAddress,"hpeServer",300)
#
import mcrpc
import ast
import os
from dotenv import load_dotenv
import re

class blockchainAccess:
    def __init__(self):
        load_dotenv()
        nodes = ast.literal_eval(os.getenv('NODES'))
        self.bank = next((node for node in nodes if node['name'] == 'bank'), None)
        self.client = c = mcrpc.RpcClient(
                self.bank['ip'], 
                self.bank['port'], 
                self.bank['user'],
                self.bank['password']
            )
        try:
            #create EUR asset class with 0 balance, issuable and devidable by 0.01 
            self.client.issue(self.client.listaddresses()[0]['address'], {"name":"EUR","open":True},0,0.01)
        except:
            pass

    def fund(self):
        def post(self, account, amount):
            self.client.issuemore(account,"EUR",amount)

    def refund(self):
        def post(self, account, amount):
            pattern = re.compile("(?<=burnaddress': ')[0-9][A-Za-z0-9]+")
            burnAddress = pattern.findall(str(self.client.getinfo()))[0]
            try:
                self.client.sendasset(burnAddress,"EUR",amount)
            except:
                return "ERROR: not enough funds available"
