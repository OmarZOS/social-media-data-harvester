

from API_ExtractionService.Extractors.UserExtractor import UserExtractor
from API_ExtractionService.Extractors.coordinatesExtractor import CoordinateExtractor
from API_ExtractionService.Extractors.mediaExtractor import MediaExtractor
from API_ExtractionService.Extractors.placeExtractor import PlaceExtractor
from API_ExtractionService.Extractors.tweetExtractor import TweetExtractor
from API_ExtractionService.Extractors.urlExtractor import URLExtractor
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

        self.graph = self.createGraph()

        if self.graph.number_of_nodes() ==0 :
            UserExtractor.crawlUser(self.firstUserID)

        #queueing before threading 

        userQueue = Queue(maxsize=0)
        userQueue.put(firstUser = self.api.get_user(user_id=self.firstUserID))
        coordinatesQueue = Queue(maxsize=0)
        placeQueue = Queue(maxsize=0)
        urlQueue = Queue(maxsize=0)
        mediaQueue  = Queue(maxsize=0)
        tweetQueue = Queue(maxsize=0)


        userAgent = Thread(target=UserExtractor.crawlUser, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        userAgent.setDaemon(True)
        userAgent.start()
        
        coordinatesAgent = Thread(target=CoordinateExtractor.crawlCoordinates, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        coordinatesAgent.setDaemon(True)
        coordinatesAgent.start()

        placeAgent = Thread(target=PlaceExtractor.crawlPlace, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        placeAgent.setDaemon(True)
        placeAgent.start()

        urlAgent = Thread(target=URLExtractor.crawlURL, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        urlAgent.setDaemon(True)
        urlAgent.start()

        mediaAgent = Thread(target=MediaExtractor.crawlMedia, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        mediaAgent.setDaemon(True)
        mediaAgent.start()

        tweetAgent = Thread(target=TweetExtractor.crawlTweet, args=(self.api,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        tweetAgent.setDaemon(True)
        tweetAgent.start()


        userQueue.join()
        userQueue.join()
        coordinatesQueue.join()
        placeQueue.join()
        urlQueue.join()
        mediaQueue.join()
        tweetQueue.join()    


        Nodeslist = [v for v in self.graph.nodes()]

        # set the waiting time
        Time=0
        Limited_number_of_followers=4000
        Limited_number_of_friends=4000

        for v in Nodeslist:
    
            try:
            
                print(" node: ",self.graph.node[user.id]['screen_name']," is it checked : ",self.graph.node[user.id]['checked'])
                # check if the node has not been check it and belong to the disired location
                if  self.graph.node[user.id]['checked'] == 0 and self.graph.node[user.id]['location'].find("Algeria") != -1 : 
                    print("Collecting data for",self.graph.node[user.id]['screen_name'],v,self.graph.node[user.id]['location'])  
                    print("The number of followers of the user are : " + str(self.graph.node[user.id]['followers_count']))
                    print("The number of followers of the user are : " + str(self.graph.node[user.id]['friends_count']))
                    if self.graph.node[user.id]['followers_count']<Limited_number_of_followers:
                        # get the follower the the user v
                        followers = []
                        for page in tweepy.Cursor(self.api.get_followers, screen_name=self.graph.node[user.id]['screen_name'], wait_on_rate_limit=True,count=300).pages():
                            try:
                                followers.extend(page)
                            except tweepy.TweepError as e:
                                print("Going to sleep:", e)
                                time.sleep(60)
                        self.graph.node[user.id]['checked']=1
                        for user in followers:
                            user.screen_name
                            Time=0                  
                            UserExtractor.insertUser(self.api,user,self.graph)

                            self.graph.add_edge(user.id,v)
                        print ("\t\tNumber Of nodes collected so far followers:", self.graph.number_of_nodes())
                        print ("\t\tNumber Of edges collected so far followers:", self.graph.number_of_edges())
                    else:
                        self.graph.node[user.id]['checked']=2
                    if self.graph.node[user.id]['friends_count']<Limited_number_of_friends:
                        # collect the list of the user v friends
                        Friends = []
                        for page in tweepy.Cursor(self.api.get_friends, screen_name=self.graph.node[user.id]['screen_name'], wait_on_rate_limit=True,count=200).pages():
                            try:
                                Friends.extend(page)
                            except tweepy.TweepError as e:
                                print("Going to sleep:", e)
                                time.sleep(60)
                        for user in Friends:
                            user.screen_name
                            Time=0
                            self.graph.node[user.id]['checked']=1
                            UserExtractor.insertUser(self.api,user,self.graph)
                            self.graph.add_edge(v,user.id)
                        print ("\t\tNumber Of nodes collected so far followers: ", self.graph.number_of_nodes())
                        print ("\t\tNumber Of edge collected so far followers: ", self.graph.number_of_edges())
                    else:
                        self.graph.node[user.id]['checked']=2
                    # nx.write_gexf(G, "Graph.gexf") 
                    # json_graph.node_link_data(G)
                    print ("\tNumber Of nodes collected so far ", self.graph.number_of_nodes())
                    print ("\tNumber Of edges collected so far", self.graph.number_of_edges())




            except tweepy.TweepError as ex: 
                if ex.reason == "Not authorized.":
                    print("exep ", ex)
                    self.graph.node[user.id]['checked']=2
                else:
                    os.system('clear')
                    print(ex)
                    print("waiting time so far : ", Time)
                    Time+=1
                    print ("Number Of nodes collected so far:", self.graph.number_of_nodes())
                    print ("Number Of edges collected so far:", self.graph.number_of_edges())
                    # nx.write_gexf(G, "Graph.gexf") 
                    # json_graph.node_link_data(G)

                    time.sleep(60)


    

    


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




        

