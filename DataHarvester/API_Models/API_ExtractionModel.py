from abc import abstractmethod
from AppLoader import ServiceLocator
from ResultListener import ResultListener


class API_extractionModel(ResultListener):
    
    storageService = ServiceLocator.storageService;
    # def __init__(self,dataModele,*args):
    #     super(*args)
    #     self.storageService = ServiceLocator.storageService;
        # self.dataModel = dataModele;

    __dataModel = {}  

        

    
    
    def dataModel(self):
        return self.__dataModel;
    
    # @property.setter
    # def dataModel(self,dataModel):
    #     self._dataModel = dataModel

    def saveData(self,data):
        self.storageService.saveData(data);
    
    @abstractmethod
    def requestByModel(fields):
        pass
    
    


        