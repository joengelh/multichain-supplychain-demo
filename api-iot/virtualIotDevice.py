import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
import random

#create IoT class
class iot:
    #define class initiation
    def __init__(self):
        #initiate sensors list
        self.sensorsList = []
        #connect to the blockchain
        #connect to banks multichain node
        load_dotenv()
        nodes = ast.literal_eval(os.getenv('NODES'))
        bank = next((node for node in nodes if node['name'] == 'iot'), None)
        self.client = c = mcrpc.RpcClient(
                bank['ip'], 
                bank['port'], 
                bank['user'],
                bank['password']
            )


    #get random measurements
    def measure(self):
        sensorData = {'temperature':0,
            'humidity':0
            'maxG':0
            'geoLocation':{'latitude':-0,
                'longditude':-0
            }
        }
        sensorData['temperature'] = uniform(14, 24)
        sensorData['humidity'] = uniform(10, 40)
        sensorData['maxG'] = uniform(0, 0.1)
        sensorData['geolocation']['latitude'] = uniform(-90, 90)
        sensorData['geolocation']['longditude'] = uniform(-180, 180)
        return sensorData

    def send(self, name):
        for sensor in self.sensorsList:
            self.client.publish(data["name"],data["key"],data["data-json"])
            self.measure

    def create(self, name):
        self.sensorsList.append(self.name)

    def destroy(self, name):
        self.sensorsList.remove(self.name)

    
