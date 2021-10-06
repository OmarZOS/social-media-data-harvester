



from abc import ABC, abstractmethod


class StorageService(ABC):
    @abstractmethod
    def saveData(data):
        pass
    @abstractmethod
    def queryData(*args):
        pass
    
        
        


