

# from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from API_Views.API_View import APi_View
from Twitter.API_Models.TwitterModel import TwitterModel
from multiprocessing import Process

class TwitterView(APi_View):

    def __init__(self,api,filePath):
        self.viewstructureFilePath = filePath;
        self.apiName = api;
        # print(self.proxy.apiName)
        modelProcess = Process(target=TwitterModel, args=(api,"omar","omar",37604))
        modelProcess.start()
        modelProcess.join
        self.initiateApiModel(modelProcess) #Process(target=TwitterModel, args=(api,"omar","omar"))
    
    def setDataStructure(self,apiJsonStruct):
        self.api_model.dataModel = apiJsonStruct

        






