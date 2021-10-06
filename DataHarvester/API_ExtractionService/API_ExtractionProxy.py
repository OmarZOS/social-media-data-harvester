from abc import abstractmethod
from API_ExtractionService import API_ExtractionService
from API_ExtractionService.API_View import APi_View

class API_ExtractionProxy(API_ExtractionService.API_ExtractionService):
    dynamicStructure = {}

    view = None
    apiName=""
    
    def StartHarvestingData(self,model):
        pass

    def getStructureFile(self):
        return self.view.viewstructureFilePath
    
    def apiView(self):
        return self.view 

    def apiView(self,s : APi_View):
        self.view = s

    def addAttribute(self,attribute):
        self.dynamicStructure.add(attribute)
    
    def removeAttribute(self,attribute):
        self.dynamicStructure.discard(attribute)
        
        


