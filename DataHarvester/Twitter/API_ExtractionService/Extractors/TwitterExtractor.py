

from networkx.classes import graph
from networkx.readwrite import json_graph
from Twitter.API_ExtractionService.Extractors.UserExtractor import UserExtractor
from Twitter.API_ExtractionService.Extractors.coordinatesExtractor import CoordinateExtractor
from Twitter.API_ExtractionService.Extractors.mediaExtractor import MediaExtractor
from Twitter.API_ExtractionService.Extractors.placeExtractor import PlaceExtractor
from Twitter.API_ExtractionService.Extractors.tweetExtractor import TweetExtractor
from Twitter.API_ExtractionService.Extractors.urlExtractor import URLExtractor
from Twitter.API_ExtractionService.Extractors.Transformers.TwitterTransformer import TwitterTransformer
from API_ExtractionService.Network_Extractor import NetworkExtractor

import time
import tweepy
import os
import networkx as nx
from queue import Queue
from threading import Thread



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

    firstUserID = "1192946702891790336" #Abd Elmadjid Tebboune



    def __init__(self,apiNam,prox,structure):
        ######################## should have been done in the abstraction
        self.proxy = prox
        self._apiName=apiNam
        print("initialising transformer..")
        self.fullStructure = structure
        self.transformer = TwitterTransformer(self._apiName,structure)
        ########################

        self.initialiseAuth()
        self.api = tweepy.API(self.auth[0])

        self.graph = nx.DiGraph(self.createGraph())

        
        userQueue = Queue(maxsize=0)
        firstUser = self.api.get_user(user_id=self.firstUserID)
        userQueue.put(firstUser)
        coordinatesQueue = Queue(maxsize=0)
        placeQueue = Queue(maxsize=0)
        urlQueue = Queue(maxsize=0)
        mediaQueue  = Queue(maxsize=0)
        tweetQueue = Queue(maxsize=0)



        if self.graph.number_of_nodes() ==0 :
            UserExtractor.crawlUser(UserExtractor,api=self.api,graph=self.graph,fullSchema=self.fullStructure,userQueue=userQueue,coordinatesQueue=coordinatesQueue,placeQueue=placeQueue,urlQueue=urlQueue,mediaQueue=mediaQueue,tweetQueue=tweetQueue)

        #queueing before threading 



        userAgent = Thread(target=UserExtractor.crawlUser, args=(self.api,self.graph,self.fullStructure,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        userAgent.setDaemon(True)
        userAgent.start()
        
        # coordinatesAgent = Thread(target=CoordinateExtractor.crawlCoordinates, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # coordinatesAgent.setDaemon(True)
        # coordinatesAgent.start()

        # placeAgent = Thread(target=PlaceExtractor.crawlPlace, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # placeAgent.setDaemon(True)
        # placeAgent.start()

        # urlAgent = Thread(target=URLExtractor.crawlURL, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # urlAgent.setDaemon(True)
        # urlAgent.start()

        # mediaAgent = Thread(target=MediaExtractor.crawlMedia, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # mediaAgent.setDaemon(True)
        # mediaAgent.start()

        tweetAgent = Thread(target=TweetExtractor.crawlTweet, args=(self.api,self.graph,self.fullStructure,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        tweetAgent.setDaemon(True)
        tweetAgent.start()


        userQueue.join()
        userQueue.join()
        coordinatesQueue.join()
        placeQueue.join()
        urlQueue.join()
        mediaQueue.join()
        tweetQueue.join()    


        

    

    


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


        

        

# Function created to extract coordinates from tweet if it has coordinate info
# Tweets tend to have null so important to run check
# Make sure to run this cell as it is used in a lot of different functions below

    def extract_coordinates(row):
        if row['Tweet Coordinates']:
            return row['Tweet Coordinates']['coordinates']
        else:
            return None

# Function created to extract place such as city, state or country from tweet if it has place info
# Tweets tend to have null so important to run check
# Make sure to run this cell as it is used in a lot of different functions below

    def extract_place(row):
        if row['Place Info']:
            return row['Place Info'].full_name
        else:
            return None




        

