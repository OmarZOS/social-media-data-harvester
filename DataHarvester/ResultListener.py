

from abc import abstractmethod
import pika
from pika.exchange_type import ExchangeType
#declaring the credentials needed for connection like host, port, username, password, exchange etc


class ResultListener:
    
    def __init__(*args,**kwargs):#,apiName,user,password,portNumber,hostName="localhost",exchange="data"
        # self.credentials = pika.PlainCredentials(user,password)
        if(len(args)>2): # to know if it was only a cast..
            print(args[5])
            args[0].connection = pika.BlockingConnection(pika.ConnectionParameters(host=args[5]))#port=portNumber, ,  credentials= self.credentials
            args[0].channel = args[0].connection.channel()
            args[0].channel.exchange_declare(args[6],  exchange_type=ExchangeType.direct)#durable=True,
            print(args[0])
            args[0].channel.basic_consume(queue=str(args[1]), on_message_callback=args[0].receiveData, auto_ack=True)
            print("starting consumption..")
            args[0].channel.start_consuming()
        
    @abstractmethod
    def receiveData(ch,method,properties,body):
        pass



        