


from API_ExtractionService.Extractors.Transformers.Publishers.PublishingService import ResultPublisher
from StorageService.neo4jService import neo4jService



class ServiceLocator:
    __instance = None
    __resultPublisher= None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if ServiceLocator.__instance == None:
            ServiceLocator()
        return ServiceLocator.__instance
    def __init__(self,*args):
        if(len(args)==1):
            """ Virtually private constructor. """
            if ServiceLocator.__instance != None:
                print("[WARNING] ServiceLocator class is a singleton! be careful..")
            else:
                ServiceLocator.__instance = self

    # @staticmethod
    def storageService(self):
        if self.storageservice == None:
            self.storageservice = neo4jService(scheme="neo4j",host_name="localhost",port=7687,user="neo4j",password="omar")
        return self.storageservice;

    def getResultPublisher(self):
        if self.__resultPublisher == None:
            self.__resultPublisher = ResultPublisher(user="omar",password="omar")
        return self.__resultPublisher;
           


if __name__ == "__main__" :

    res = ServiceLocator;
    print(ServiceLocator(ServiceLocator))
    print(ServiceLocator(ServiceLocator))
    print(ServiceLocator(ServiceLocator))
    print(ServiceLocator(ServiceLocator))
    print(ServiceLocator(ServiceLocator))
    print(res);
    print(res);





