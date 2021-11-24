
# from Twitter.API_ExtractionService.Extractors.Transformers.TwitterTransformer import TwitterTransformer
from AppLoader import ServiceLocator
from Twitter.API_Controllers.TwitterController import TwitterController
from Youtube.API_Controllers.YoutubeController import YoutubeController



def testTwitter():
    controller = TwitterController("Twitter");
    print(controller.extractionService.serviceName())
    controller.extractionService.StartHarvestingData()
    ServiceLocator().getResultPublisher().publish("Twitter","seasons they will change")
    ServiceLocator().getResultPublisher().publish("Twitter","bitte lass mich alein..")
    ServiceLocator().getResultPublisher().publish("Twitter","It took all the strength man hat not to fall apart..")


def testYoutube():
    controller = YoutubeController("Youtube");
    print(controller.extractionService.serviceName())
    controller.extractionService.StartHarvestingData()
    ServiceLocator().getResultPublisher().publish("Youtube","When the cards all fold")
    ServiceLocator().getResultPublisher().publish("Youtube","Dazu habt ihr gewollten..")
    ServiceLocator().getResultPublisher().publish("Youtube","Dafur bin ich der richtige..")




locator = ServiceLocator("launch");# passing this parameter just to avoid recreation
#it may be the first place to inspect by a visitor..

if __name__=="__main__":

    #testTwitter()
    testYoutube()