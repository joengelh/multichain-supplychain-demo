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

lock = client.preparelockunspent({"hpeServer":1})
#print(lockresult["txid"])
#print(lockresult["vout"])
rawExchange = client.createrawexchange(lock["txid"],lock["vout"],{"EUR":25000})
print(rawExchange)