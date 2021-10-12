from abc import abstractmethod
from AppLoader import ServiceLocator
from ResultListener import ResultListener


class API_extractionModel(ResultListener):
    
    storageService = ServiceLocator.storageService;

    __dataModel = {}  

        

    
    
    def dataModel(self):
        return self.__dataModel;
    
    def saveData(self,data):
        self.storageService.saveData(data);
    
    @abstractmethod
    def requestByModel(fields):
        pass
    
    


        