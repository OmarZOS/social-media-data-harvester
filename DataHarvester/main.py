
# from Twitter.API_ExtractionService.Extractors.Transformers.TwitterTransformer import TwitterTransformer
from AppLoader import ServiceLocator
from Twitter.API_Controllers.TwitterController import TwitterController


locator = ServiceLocator();
#may be the first place to visit

controller = TwitterController("Twitter");
print(controller.extractionService.serviceName())
controller.extractionService.StartHarvestingData()
ServiceLocator().getResultPublisher().publish("Twitter","seasons they will change")
ServiceLocator().getResultPublisher().publish("Twitter","Life can make you pay")
