


from API_ExtractionService.API_ExtractionProxy import API_ExtractionProxy
from API_ExtractionService.API_View import APi_View
from API_Models.FacebookModel import FacebookModel
from multiprocessing import Process

class FacebookView(APi_View):

    def __init__(self,api,filePath):
        self.viewstructureFilePath = filePath;
        self.apiName = api;
        # print(self.proxy.apiName)
        modelProcess = Process(target=FacebookModel, args=(api,"omar","omar",37604))
        modelProcess.start()
        modelProcess.join
        self.initiateApiModel(modelProcess) #Process(target=FacebookModel, args=(api,"omar","omar"))
    
    def setDataStructure(self,apiJsonStruct):
        self.api_model.dataModel = apiJsonStruct

        






