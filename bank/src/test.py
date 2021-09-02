import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask
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

def fund(account, amount):
    client.issuemore(account,"EUR",amount)


def balance(account):
    client.importaddress(account)
    print(client.getaddressbalances(account))

def refund(amount):
    pattern = re.compile("(?<=burnaddress': ')[0-9][A-Za-z0-9]+")
    burnAddress = pattern.findall(str(client.getinfo()))[0]
    client.sendasset(burnAddress,"EUR",amount)
refund(1)
