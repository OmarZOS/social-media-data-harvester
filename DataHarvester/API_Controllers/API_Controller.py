
from abc import ABC
# import collections
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy

class API_Controller(ABC):
    
    
    def __init__(self,prox : API_ExtractionProxy):
        self._extractionService = prox
        # self.getStructure()

    # @property
    # def extractionService(self):
    #     return self._extractionService
    # @property.setter
    # def extractionService(self,extractServ : API_ExtractionService):
    #     self._extractionService = extractServ

    def getStructureFilePathName(self):
        return self._extractionService.getStructureFilePath;
    
    
    
        