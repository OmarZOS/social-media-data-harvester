

from API_ExtractionService.Extractors.Transformers.FacebookTransformer import FacebookTransformer
from API_ExtractionService.Network_Extractor import NetworkExtractor


class FacebookExtractor(NetworkExtractor):
    
    def __init__(self,apiNam,prox,structure):
        self.proxy = prox
        self._apiName=apiNam
        print("initialising transformer..")
        self.transformer = FacebookTransformer(self.apiName,structure)
        

    def initTransformer(self,structure):
        return FacebookTransformer(self.apiName,structure)
    
    def connectAPI(key):
        pass
        

