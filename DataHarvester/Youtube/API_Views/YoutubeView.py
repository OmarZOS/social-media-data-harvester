

# from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from API_Views.API_View import APi_View
from Youtube.API_Models.YoutubeModel import YoutubeModel
from multiprocessing import Process

class YoutubeView(APi_View):

    def __init__(self,api,filePath):
        self.viewstructureFilePath = filePath;
        self.apiName = api;
        # print(self.proxy.apiName)
        modelProcess = Process(target=YoutubeModel, args=(api,"omar","omar",37604,"localhost","data"))
        modelProcess.start()
        modelProcess.join
        self.initiateApiModel(modelProcess) #Process(target=YoutubeModel, args=(api,"omar","omar"))
    
    def setDataStructure(self,apiJsonStruct):
        self.customDataModel = apiJsonStruct
        

        






