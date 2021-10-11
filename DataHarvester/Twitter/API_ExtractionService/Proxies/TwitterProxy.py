
import json
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from API_Models.API_ExtractionModel import API_extractionModel
from Twitter.API_ExtractionService.Extractors.TwitterExtractor import TwitterExtractor
from Twitter.API_Views.TwitterView import TwitterView

class TwitterProxy(API_ExtractionProxy):


    def __init__(self,apiName):
        # super(apiName)
        self.apiName = apiName
        print(apiName)
        self.apiView = TwitterView(api= apiName,filePath = "somewhere.json")
        # self.fullStructure = API_extractionModel(self.apiView.api_model).dataModel


    def StartHarvestingData(self):
        with open("Twitter/API_Models/TwitterSchema.json") as f:
            self.fullStructure = json.load(f)
         #a workaround to avoid sharing data with the model
        print((self.fullStructure).keys())
        self._networkExtractor  = TwitterExtractor(self.apiName,self,self.fullStructure)

    def setDataStructure(self,apiJsonStruct): #custom schema
        self.dataModel = apiJsonStruct


    

    


        
        