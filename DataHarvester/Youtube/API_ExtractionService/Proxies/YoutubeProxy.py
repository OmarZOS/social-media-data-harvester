
import json
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from API_Models.API_ExtractionModel import API_extractionModel
from Youtube.API_ExtractionService.Extractors.YoutubeExtractor import YoutubeExtractor
from Youtube.API_Views.YoutubeView import YoutubeView

class YoutubeProxy(API_ExtractionProxy):


    def __init__(self,apiName):
        # super(apiName)
        self.apiName = apiName
        print(apiName)
        self.apiView = YoutubeView(api= apiName,filePath = "somewhere.json")
        # self.fullStructure = API_extractionModel(self.apiView.api_model).dataModel


    def StartHarvestingData(self):
        with open("Youtube/API_Models/YoutubeSchema.json") as f:
            self.fullStructure = json.load(f)
         #a workaround to avoid sharing data with the model
        print((self.fullStructure).keys())
        self._networkExtractor  = YoutubeExtractor(self.apiName,self,self.fullStructure)

    def setDataStructure(self,apiJsonStruct): #custom schema
        self.dataModel = apiJsonStruct


    

    


        
        