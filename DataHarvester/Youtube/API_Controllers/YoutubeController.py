

from API_Controllers.API_Controller import API_Controller
from Youtube.API_ExtractionService.Proxies.YoutubeProxy import YoutubeProxy




class YoutubeController(API_Controller):
    _extractionService = None
    def __init__(self,apiname):
        # super(YoutubeProxy(apiname))
        self._extractionService = YoutubeProxy(apiname)
        
    @property
    def extractionService(self):
        return self._extractionService





if __name__=="__main__":
    controller = YoutubeController("Youtube");
    print(controller.extractionService.serviceName)



