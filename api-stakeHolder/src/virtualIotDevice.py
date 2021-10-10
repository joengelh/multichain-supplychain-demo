import mcrpc
import os
from dotenv import load_dotenv
import re
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
import random
import time
import threading

#create IoT class
class iot:
    #define class initiation
    def __init__(self):
        #initiate sensors list
        self.sensorsList = []
        #connect to the blockchain
        load_dotenv()
        nodes = ast.literal_eval(os.getenv('NODES'))
        iot = next((node for node in nodes if node['name'] == 'iot'), None)
        self.client = c = mcrpc.RpcClient(
                iot['ip'], 
                iot['port'], 
                iot['user'],
                iot['password']
            )
        thread = threading.Thread(target=self.send, args=())
        # Daemonize thread
        thread.daemon = True
        thread.start()

    #get random measurements
    def measure(self):
        #create dict for filling randomly later
        sensorData = {'json':{'temperature':0,
            'humidity':0,
            'maxG':0,
            'geoLocation':{'latitude':-0,
                'longditude':-0
            },
            'syslog':""
        }
        }
        
        #get syslog files
        with open('/var/log/syslog') as f:
            lines = f.readlines()
            f.close()

        #fill dict with random measurements
        sensorData['json']['temperature'] = random.uniform(14, 24)
        sensorData['json']['humidity'] = random.randint(10,22)
        sensorData['json']['maxG'] = random.uniform(0, 0.1)
        sensorData['json']['geoLocation']['latitude'] = random.uniform(-90, 90)
        sensorData['json']['geoLocation']['longditude'] = random.uniform(-180, 180)
        sensorData['json']['syslog'] = str(lines[-1])
        return sensorData

    def send(self):
        while True:
            for sensor in self.sensorsList:
                self.client.publish(sensor,"sensor",self.measure())
            time.sleep(10)

    def create(self, name):
        if name not in self.sensorsList:
            try:
                self.client.create("stream",name,False)
            except:
                pass
    
    def activate(self,name):
        if name not in self.sensorsList:
            self.create(name)
            result = self.sensorsList.append(name)
            return result
        else: 
            return "Sensor already active." 

    def deactivate(self, name):
        self.sensorsList.remove(name)

    def listActive(self):
        return self.sensorsList

    def listItems(self, name):
        if name in self.sensorsList:
            result = self.client.liststreamitems(name)
            return result
        else:
            return "Sensor not active."
