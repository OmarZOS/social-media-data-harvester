



class TweetExtractor:
    fullStructure = None
    @staticmethod
    def crawlTweet(self,api,fullStructure,uid,graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue):
        self.fullStructure = fullStructure
        while True:
            freshTweet = tweetQueue.get()
            # TweetExtractor.insertTweet(freshTweet,graph)
            
            # entities = freshTweet["entities"]
            
            #TODO : 
            # hashtags_list = []
            # for hashtag in entities["hashtags"] :
            #     placeQueue.put(hashtag["text"])
            
            #TODO : 
            # urls_list = []
            # for url in entities["urls"]:
            #     urlQueue.put(url)
            
            #TODO : 
            # media_list = {}
            # if 'media' in entities :
            #     for media in entities["media"]:
            #         mediaQueue.put(media)
            
            #TODO :             
            # user_mentions_list = []
            # for user_mention in entities["user_mentions"]:
            #     user_mentions_list.append(user_mention["screen_name"])
            # self.user_mentions = user_mentions_list

            #TODO :             
            # coordinates_list = []
            # for coordinate in entities["coordinates"]:
            #     coordinatesQueue.put(coordinate)

            tweetQueue.task_done()




    @staticmethod
    def insertTweet(self,tweet,graph): # verifies existence inside
        attributes = {}
        if(tweet.id in graph): #nothing to do here
            return 
        for attribute in TweetExtractor.fullStructure["tweet"]:
            attributes[attribute+""] = tweet[attribute]

        graph.add_edges_from([(tweet.id,attributes)])

        
        
