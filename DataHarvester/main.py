
from API_ExtractionService.Extractors.Transformers.FacebookTransformer import FacebookTransformer
from AppLoader import ServiceLocator
from API_Controllers.FacebookController import FacebookController

locator = ServiceLocator();
#may be the first place to visit

controller = FacebookController("Facebook");
print(controller.extractionService.serviceName())
controller.extractionService.StartHarvestingData()
ServiceLocator().getResultPublisher().publish("Facebook","zeafsq")
ServiceLocator().getResultPublisher().publish("Facebook","deydey")
