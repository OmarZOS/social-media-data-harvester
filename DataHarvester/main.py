
# from Twitter.API_ExtractionService.Extractors.Transformers.TwitterTransformer import TwitterTransformer
from AppLoader import ServiceLocator
from Twitter.API_Controllers.TwitterController import TwitterController



locator = ServiceLocator("launch");# passing this parameter just to avoid recreation
#may be the first place to visit

controller = TwitterController("Twitter");
print(controller.extractionService.serviceName())
controller.extractionService.StartHarvestingData()
ServiceLocator().getResultPublisher().publish("Twitter","seasons they will change")
ServiceLocator().getResultPublisher().publish("Twitter","bitte lass mich alein..")
ServiceLocator().getResultPublisher().publish("Twitter","not to fall apart..")