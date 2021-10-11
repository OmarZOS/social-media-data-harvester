


import json
import os
import time
import networkx
import tweepy



class UserExtractor:

    # set the waiting time
    Time=0
    Limited_number_of_followers=4000
    Limited_number_of_friends=4000
    fullStructure = None


    @staticmethod
    def crawlUser(self,api,graph,fullSchema,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue):
        UserExtractor.fullStructure = fullSchema

        # print(api)
        # print(fullSchema)
        # print(userQueue)
        # print(coordinatesQueue)

        while True:
            freshUser = userQueue.get()


            UserExtractor.insertUser(user=freshUser,graph=graph)


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
                print("The number of followers of the user are : " , freshUser.friends_count)
                
                UserExtractor.scrapFollowers(freshUser,api,graph)
                UserExtractor.scrapFriends(freshUser,api,graph)

                #getting the timeline..
                usertweets = api.user_timeline(screen_name=freshUser.screen_name, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

                for tweet in usertweets:
                    tweetQueue.put(tweet)
                    

                

            except tweepy.TweepError as ex: 
                if ex.reason == "Not authorized.":
                    print("exep ", ex)
                else:
                    os.system('clear')
                    print(ex)
                    print("waiting time so far : ", UserExtractor.Time)
                    UserExtractor.Time+=1
                    print ("Number Of nodes collected so far:", graph.number_of_nodes())
                    print ("Number Of edges collected so far:", graph.number_of_edges())
                    # nx.write_gexf(G, "Graph.gexf") 
                    # json_graph.nodes_link_data(G)

                    time.sleep(60)

            userQueue.task_done()





    @staticmethod    
    def insertUser(graph : networkx.DiGraph,user : tweepy.User): # verifies existence inside
        attributes = {}
        # user= json.dumps(user)

        # print(user.id)
        # print(graph)
        # print(UserExtractor.fullStructure)
        if(user.id in graph): #nothing to do here
            return 
        for attribute in UserExtractor.fullStructure["user"]:
            attributes[str(attribute)+""] = getattr(user,attribute)
        

        # print(attributes)
        
        # print(attributes.items())
        graph.add_edges_from([(user.id,tuple(attributes))])

    @staticmethod
    def scrapFriends(freshUser,api,graph):
        if graph[freshUser.id]['friends_count']<UserExtractor.Limited_number_of_friends:
            # collect the list of the user v friends
            Friends = []
            for page in tweepy.Cursor(api.get_friends, screen_name=graph.nodes[freshUser.id]['screen_name'], wait_on_rate_limit=True,count=200).pages():
                try:
                    Friends.extend(page)
                except tweepy.TweepError as e:
                    print("Going to sleep:", e)
                    time.sleep(60)
            for user in Friends:
                user.screen_name
                Time=0
                # graph.nodes[user.id]['checked']=1
                UserExtractor.insertUser(graph=graph,user=user)
                graph.add_edge(freshUser,user.id,other= "friend")
            print ("\t\tNumber Of nodes collected so far followers: ", graph.number_of_nodes())
            print ("\t\tNumber Of edge collected so far followers: ", graph.number_of_edges())
            # nx.write_gexf(G, "Graph.gexf") 
            # json_graph.nodes_link_data(G)
            print ("\tNumber Of nodes collected so far ", graph.number_of_nodes())
            print ("\tNumber Of edges collected so far", graph.number_of_edges())

    @staticmethod
    def scrapFollowers(freshUser,api,graph):
        if graph[freshUser.id]['followers_count']<UserExtractor.Limited_number_of_followers:
            # get the follower the the user
            followers = []
            for page in tweepy.Cursor(api.get_followers, screen_name=graph.nodes[freshUser.id]['screen_name'], wait_on_rate_limit=True,count=300).pages():
                try:
                    followers.extend(page)
                except tweepy.TweepError as e:
                    print("Going to sleep:", e)
                    time.sleep(60)
            for user in followers:
                user.screen_name
                Time=0                  
                UserExtractor.insertUser(user=user,graph=graph)

                graph.add_edge(user.id,freshUser,other= "follows")
            print ("\t\tNumber Of nodes collected so far followers:", graph.number_of_nodes())
            print ("\t\tNumber Of edges collected so far followers:", graph.number_of_edges())


