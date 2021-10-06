

from abc import abstractmethod
import pika
from pika.exchange_type import ExchangeType
#declaring the credentials needed for connection like host, port, username, password, exchange etc


class ResultListener:
    
    def __init__(self,apiName,user,password,portNumber,hostName="localhost",exchange="data"):
        # self.credentials = pika.PlainCredentials(user,password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName))#port=portNumber, ,  credentials= self.credentials
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange,  exchange_type=ExchangeType.direct)#durable=True,
        self.channel.basic_consume(queue=str(apiName), on_message_callback=self.receiveData, auto_ack=True)
        print("starting consumption..")
        self.channel.start_consuming()
        
    @abstractmethod
    def receiveData(ch,method,properties,body):
        pass



        