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
bank = next((node for node in nodes if node['name'] == 'serviceProvider'), None)
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

#client.issuemore(client.listaddresses()[0]['address'],"hpeServer",100)
#print(client.getmultibalances())
#for server in tradableServers:
    #issue asset class for every server, quantitiy zero, devisible by 1
#    client.issue(client.listaddresses()[0]['address'], {"name":server,"open":True},0,1)
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"dellserver",600,1)
#client.sendasset(burnAddress,"hpeServer",300)

