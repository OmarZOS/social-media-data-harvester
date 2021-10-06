
from neo4j import GraphDatabase



from StorageService.StorageService import StorageService


class neo4jService(StorageService):

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def saveData(args):
        pass       

    def queryData(*args):
        pass



