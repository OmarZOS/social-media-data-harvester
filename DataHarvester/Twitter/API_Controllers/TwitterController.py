

from API_Controllers.API_Controller import API_Controller
from Twitter.API_ExtractionService.Proxies.TwitterProxy import TwitterProxy




class TwitterController(API_Controller):
    _extractionService = None
    def __init__(self,apiname):
        # super(TwitterProxy(apiname))
        self._extractionService = TwitterProxy(apiname)
        
    @property
    def extractionService(self):
        return self._extractionService





if __name__=="__main__":
    controller = TwitterController("Twitter");
    print(controller.extractionService.serviceName)



