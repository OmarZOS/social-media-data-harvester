


import json
import os
from queue import Queue
import time
import networkx
import random
import tweepy



class UserExtractor:

    # set the waiting time
    Time=0
    Limited_number_of_followers=4000
    Limited_number_of_friends=4000
    fullStructure = None


    @staticmethod
    def crawlUser(api,graph,fullSchema,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue):
        UserExtractor.fullStructure = fullSchema

        # print(api)
        # print(fullSchema)
        # print(userQueue)
        # print(coordinatesQueue)
        freshUser = userQueue.get()
        UserExtractor.insertUser(user=freshUser,graph=graph)

        while True:
            # print("again")
            print(freshUser.screen_name)



            # coordinatesQueue.put(freshUser.)
            # placeQueue
            # geoQueue
            # mediaQueue
            # tweetQueue

            try:

                print(" node: ",freshUser.screen_name," is it checked : ","no")
                # check if the node has not been check it and belong to the disired location
                # print(graph)
                print("Collecting data for",freshUser.screen_name,freshUser.id,freshUser.location)  
                print("The number of followers of the user are : " , freshUser.followers_count)
                print("The number of friends of the user are : " , freshUser.friends_count)
                
                UserExtractor.scrapFollowers(freshUser,api,graph,userQueue)
                
                UserExtractor.scrapFriends(freshUser,api,graph,userQueue)

                # getting the timeline..
                # usertweets = api.user_timeline(screen_name=freshUser.screen_name, 
                #            # 200 is the maximum allowed count
                #            count=200,
                #            include_rts = False,
                #            # Necessary to keep full_text 
                #            # otherwise only the first 140 words are extracted
                #            tweet_mode = 'extended'
                #            )

                # if(UserExtractor.fullStructure["tweet"]):
                #     for tweet in usertweets:
                #         print("adding a tweet")
                #         # graph.add_edge(freshUser.id,tweet.id,other= "published")#done inside tweetExtractor
                #         tweetQueue.put(tweet)

                    


            except tweepy.TweepyException as ex: 
                print("\033[93m An exception has occured \030[93m")
                print(ex.with_traceback)

                #emptying the queue to terminate the thread..
                while not userQueue.empty():
                    userQueue.task_done()
                    
                    userQueue.get()
                


                # if ex. == "Not authorized.":
                #     print("exep ", ex)
                # else:
                #     os.system('clear')
                #     print(ex)
                #     print("waiting time so far : ", UserExtractor.Time)
                #     UserExtractor.Time+=1
                    
                #     print ("Number Of nodes collected so far:", graph.number_of_nodes())
                #     print ("Number Of edges collected so far:", graph.number_of_edges())
                #     # nx.write_gexf(G, "Graph.gexf") 
                #     # json_graph.nodes_link_data(G)

                #     time.sleep(60)
            # print("done scraping")
            userQueue.task_done()
            freshUser = userQueue.get()




    # count = 0

    @staticmethod
    def insertUser(graph : networkx.DiGraph,user : tweepy.User): # verifies existence inside
        # a workaround to limit token usage..
        # UserExtractor.count+=1
        # if UserExtractor.count > 5 :
        #     raise tweepy.TweepyException();
        
        attributes = {}
        # user= json.dumps(user)

        # print(user.id)
        # print(graph)
        # print(UserExtractor.fullStructure)
        if(user.id in graph): #nothing to do here
            return 
        for attribute in UserExtractor.fullStructure["user"]:
            attributes[str(attribute)+""] = str(getattr(user,attribute))
        

        # print(attributes)
        
        # print(attributes.items())
        if(len(attributes.items()) > 2) :
            graph.add_nodes_from([(user.id,[k for k in attributes.items()])],color="green")

    @staticmethod
    def scrapFriends(freshUser,api,graph,userQueue:Queue):
        # if freshUser.friends_count<UserExtractor.Limited_number_of_friends:
        # collect the list of the user v friends
        Friends = []
        for page in tweepy.Cursor(api.get_friends, screen_name=freshUser.screen_name,count=100).pages():
            try:
                Friends.extend(page)
            except tweepy.TweepError as e:
                print("Going to sleep:", e)
                time.sleep(60)
        for user in Friends:
            if random.randrange(0,4) !=0 :
                continue;
            print(user.screen_name)
            Time=0
            # graph.nodes[user.id]['checked']=1
            UserExtractor.insertUser(graph=graph,user=user)
            userQueue.put(user)
            graph.add_edge(freshUser.id,user.id,other= "friend")
        print ("\t\tNumber Of nodes collected so far followers: ", graph.number_of_nodes())
        print ("\t\tNumber Of edge collected so far followers: ", graph.number_of_edges())
        # nx.write_gexf(G, "Graph.gexf") 
        # json_graph.nodes_link_data(G)
        print ("\tNumber Of nodes collected so far ", graph.number_of_nodes())
        print ("\tNumber Of edges collected so far", graph.number_of_edges())

    @staticmethod
    def scrapFollowers(freshUser:tweepy.User,api,graph,userQueue):
        # if freshUser.followers_count<UserExtractor.Limited_number_of_followers:
            # get the followers of the user
        followers = []
        for page in tweepy.Cursor(api.get_followers, screen_name=freshUser.screen_name, wait_on_rate_limit=True,count=100).pages():
            try:
                followers.extend(page)
            except tweepy.TweepError as e:
                print("Going to sleep:", e)
                time.sleep(60)
        for user in followers:
            if random.randrange(0,4) !=0 :
                continue;
            user.screen_name
            Time=0                  
            UserExtractor.insertUser(user=user,graph=graph)
            userQueue.put(user)

            graph.add_edge(user.id,freshUser.id,other= "follows")
        print ("\t\tNumber Of nodes collected so far followers:", graph.number_of_nodes())
        print ("\t\tNumber Of edges collected so far followers:", graph.number_of_edges())


