import mcrpc
import ast
import os
from dotenv import load_dotenv
import re

load_dotenv()
nodes = ast.literal_eval(os.getenv('NODES'))

tradableServers = ['hpeServer','dellServer','ciscoServer']

client = c = mcrpc.RpcClient(
        nodes[0]['ip'], 
        nodes[0]['port'], 
        nodes[0]['user'],
        nodes[0]['password']
    )

#get burnAddress
pattern = re.compile("(?<=burnaddress': ')[0-9][A-Za-z0-9]+")
burnAddress = pattern.findall(str(client.getinfo()))[0]

for server in tradableServers:
    try:        
        #issue asset class for every server, quantitiy zero, devisible by 1
        client.issue(client.listaddresses()[0]['address'], {"name":server,"open":True},0,1)
    except:
        print("asset already exists")

print(client.getmultibalances())

#client.issuemore(client.listaddresses()[0]['address'],"hpeServer",100)

#print(client.getmultibalances())

#for server in tradableServers:
    #issue asset class for every server, quantitiy zero, devisible by 1
#    client.issue(client.listaddresses()[0]['address'], {"name":server,"open":True},0,1)
#client.create("steam","iot001",False)
#client.issue(client.listaddresses()[0]['address'],"dellserver",600,1)
client.sendasset(burnAddress,"hpeServer",300)
