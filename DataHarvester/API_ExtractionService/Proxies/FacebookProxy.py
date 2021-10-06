
from API_ExtractionService.API_ExtractionProxy import API_ExtractionProxy
from API_ExtractionService.Extractors.FacebookExtractor import FacebookExtractor
from API_Views.FacebookView import FacebookView

class FacebookProxy(API_ExtractionProxy):


    def __init__(self,apiName):
        # super(apiName)
        self.apiName = apiName
        print(apiName)
        self.apiView = FacebookView(api= apiName,filePath = "somewhere.json")


    def StartHarvestingData(self):
        self._networkExtractor  = FacebookExtractor(self.apiName,self,self.dynamicStructure)




    

    


        
        