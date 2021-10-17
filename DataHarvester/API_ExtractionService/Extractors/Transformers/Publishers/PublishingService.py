

import pika
from pika.exchange_type import ExchangeType
from pika.spec import Queue


class ResultPublisher:
    def __init__(self,user="omar",password="omar",*args):
        pass
        self.credentials = pika.PlainCredentials(user,password)
        self.connection= pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))#, credentials= self.credentials
        self.channel= self.connection.channel()
    
        self.channel.exchange_declare(exchange='data', exchange_type=ExchangeType.direct)
        

    
    def addQueue(self,apiName):
        self.channel.queue_declare(queue= apiName)
        self.channel.queue_bind(exchange="data", queue=apiName, routing_key=apiName)
        
    
    def publish(self,api,data):
        # print("publishing")
        self.channel.basic_publish(exchange="data",routing_key = api, body = data)
            
    
        

    


