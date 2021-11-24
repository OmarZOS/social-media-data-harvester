

import json
from networkx.classes import graph
from networkx.readwrite import json_graph
from Youtube.API_ExtractionService.Extractors.ChannelExtractor import ChannelExtractor
from Youtube.API_ExtractionService.Extractors.Transformers.YoutubeTransformer import YoutubeTransformer
from API_ExtractionService.Network_Extractor import NetworkExtractor

import time
import os
import networkx as nx
from queue import Queue
from threading import Thread

from Youtube.API_ExtractionService.Extractors.termSeeker import termSeeker




class YoutubeExtractor(NetworkExtractor):
    
    api_key=[]


    def __init__(self,apiNam,prox,structure):
        ######################## should have been done in the abstraction
        self.proxy = prox
        self._apiName=apiNam
        print("initialising transformer..")
        self.fullStructure = structure
        self.transformer = YoutubeTransformer(self._apiName,structure)
        ########################

        self.initialiseAuth()

        self.graph = nx.DiGraph(self.createGraph())

        termQueue = Queue(maxsize=0) # 0 for infinite
        channelQueue = Queue(maxsize=0)
        videoQueue = Queue(maxsize=0)
        playlistQueue = Queue(maxsize=0)
        commentQueue = Queue(maxsize=0)
        replyQueue  = Queue(maxsize=0)

        # firstUser = self.api.get_user(user_id=self.firstUserID)
        
        termQueue.put("lotfi dk")


        # if self.graph.number_of_nodes() ==0 :
        #     UserExtractor.crawlUser(UserExtractor,api=graph=self.graph,fullSchema=self.fullStructure,termQueue=termQueue,channelQueue=channelQueue,playlistQueue=videoQueue,playlistQueue,commentQueue=commentQueue,replyQueue=replyQueue)

        #queueing before threading 

        termAgent = Thread(target=termSeeker.searchTerm, args=(self.graph,self.fullStructure,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue))
        termAgent.setDaemon(True)
        termAgent.start()
        
        videoAgent = Thread(target=VideoExtractor.crawlChannel, args=(self.graph,self.fullStructure,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue,ChannelQueue))
        videoAgent.setDaemon(True)
        videoAgent.start()
        
        channelAgent = Thread(target=ChannelExtractor.crawlChannel, args=(self.graph,self.fullStructure,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue,ChannelQueue))
        channelAgent.setDaemon(True)
        channelAgent.start()
        
        playlistAgent = Thread(target=PlaylistExtractor.crawlPlaylist, args=(self.fullStructure,self.graph,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue,ChannelQueue))
        playlistAgent.setDaemon(True)
        playlistAgent.start()
        

        # commentAgent = Thread(target=commentExtractor.crawlcomment, args=(self.fullStructure,self.graph,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue,ChannelQueue))
        # commentAgent.setDaemon(True)
        # commentAgent.start()
        
        # replyAgent = Thread(target=replyExtractor.crawlreplys, args=(self.fullStructure,self.graph,termQueue,channelQueue,videoQueue,playlistQueue,commentQueue,replyQueue,ChannelQueue))
        # replyAgent.setDaemon(True)
        # replyAgent.start()


        termQueue.join()
        videoQueue.join()    
        channelQueue.join()    
        playlistQueue.join()
        commentQueue.join()
        replyQueue.join()

        print("Extraction complete.")
        self.save_json("Graph.json",self.graph)

    def initialiseAuth(self):
        self.api_key.append(str(os.getenv("YOUTUBE_KEY")))
        

    def createGraph(self):
        return nx.DiGraph()
        

    def initTransformer(self,structure):
        return YoutubeTransformer(self.apiName,structure)
    
    def connectAPI(key):
        pass

    def save_json(self,filename,graph):
        g = graph
        g_json = json_graph.node_link_data(g)
        json.dump(g_json,open(filename,'w'),indent=2)

        

        






        

