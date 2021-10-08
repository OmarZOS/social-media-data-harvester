
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from Twitter.API_ExtractionService.Extractors.TwitterExtractor import TwitterExtractor
from Twitter.API_Views.TwitterView import TwitterView

class TwitterProxy(API_ExtractionProxy):


    def __init__(self,apiName):
        # super(apiName)
        self.apiName = apiName
        print(apiName)
        self.apiView = TwitterView(api= apiName,filePath = "somewhere.json")


    def StartHarvestingData(self):
        self._networkExtractor  = TwitterExtractor(self.apiName,self,self.dynamicStructure)




    

    


        
        