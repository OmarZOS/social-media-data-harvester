

from API_Controllers.API_Controller import API_Controller
from API_ExtractionService.Proxies.FacebookProxy import FacebookProxy




class FacebookController(API_Controller):
    _extractionService = None
    def __init__(self,apiname):
        # super(FacebookProxy(apiname))
        self._extractionService = FacebookProxy(apiname)
        
    @property
    def extractionService(self):
        return self._extractionService





if __name__=="__main__":
    controller = FacebookController("Facebook");
    print(controller.extractionService.serviceName)



