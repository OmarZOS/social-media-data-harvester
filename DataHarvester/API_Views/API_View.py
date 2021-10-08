

from API_Models.API_ExtractionModel import API_extractionModel
# from API_ExtractionModel import API_ExtractionModel

from abc import ABC,abstractmethod  
class APi_View(ABC):
    viewstructureFilePath = ""
    
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def setDataStructure(self,apiJsonStruct):
        pass;

    @property
    def getStructureFile(self):
        return self.viewstructureFilePath;

    
    def initiateApiModel(self, model : API_extractionModel):
        self.api_model = model;
    
    

        




        


        