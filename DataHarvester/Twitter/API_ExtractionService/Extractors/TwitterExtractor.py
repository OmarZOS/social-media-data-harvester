

from Twitter.API_ExtractionService.Extractors.Transformers.TwitterTransformer import TwitterTransformer
from API_ExtractionService.Network_Extractor import NetworkExtractor

import time
import tweepy
import os
import networkx as nx




class TwitterExtractor(NetworkExtractor):
    
    consumer_key=[]
    consumer_secret=[]
    access_key=[]
    access_secret=[]
    consumer_key.append("aRPAzCMKhotCBKqlStSk1IN8S")
    consumer_secret.append("UAo5USjuLKE6SzIlw7EpCklZF8MeYg8kLv4KUqZAMcU4cSPTNr")
    access_key.append("1440700278613839878-QuYijjPLUXgWbTTvVYQaBaZJnX7zcl")
    access_secret.append("Z5rKjgfClqcmaSfKdebnkqsmsBpCV9FqspRYhLCaHixHR")

    auth = []

    def __init__(self,apiNam,prox,structure):
        ######################## should have been done in the abstraction
        self.proxy = prox
        self._apiName=apiNam
        print("initialising transformer..")
        self.transformer = TwitterTransformer(self.apiName,structure)
        ########################

        self.initialiseAuth()
        self.api = tweepy.API(self.auth[0])

        self.graph = self.createGraph()

    

        


    def initialiseAuth(self):
        for i in range(len(self.consumer_key)):
            self.auth.append(tweepy.OAuthHandler(self.consumer_key[i], self.consumer_secret[i]))
        self.auth[i].set_access_token(self.access_key[i], self.access_secret[i])

    def createGraph(self):
        return nx.DiGraph()
        

    def initTransformer(self,structure):
        return TwitterTransformer(self.apiName,structure)
    
    def connectAPI(key):





        pass
        

