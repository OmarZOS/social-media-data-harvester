from abc import abstractmethod
from AppLoader import ServiceLocator
from ResultListener import ResultListener


class API_extractionModel(ResultListener):
    
    storageService = ServiceLocator.storageService;
    # def __init__(self,dataModele,*args):
    #     super(*args)
    #     self.storageService = ServiceLocator.storageService;
        # self.dataModel = dataModele;
        
    @property
    def dataModel(self):
        return self.dataModel;
    
    # @property.setter
    def dataModel(self,dataModel):
        self.dataModel = dataModel

    def saveData(self,data):
        self.storageService.saveData(data);
    
    @abstractmethod
    def requestByModel(fields):
        pass
    
    


        