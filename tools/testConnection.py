import mcrpc
import ast
import os
from dotenv import load_dotenv
import re

load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))

for node in nodes:
    try:
        client = c = mcrpc.RpcClient(
            node['ip'], 
            node['port'], 
            node['user'],
            node['password']
        )
        print(client.getinfo())
    except: print(node, " offline")
