
from abc import ABC, abstractmethod
from API_ExtractionService.Extractors.Transformers.Publishers.PublishingService import ResultPublisher

from AppLoader import ServiceLocator

class API_Transformer(ABC):
    
    def __init__(self,apiName,dataModel,*args) :
        self.dataModel = dataModel
        locator = ServiceLocator(ServiceLocator.getInstance())
        self.publisher = ResultPublisher(locator.getResultPublisher());
        self.apiName = apiName
        print("setting queue : "+apiName)
        self.publisher.addQueue(apiName)
        
    def diffuseData(self,data):
        self.publisher.publish(data,self.apiName,data)