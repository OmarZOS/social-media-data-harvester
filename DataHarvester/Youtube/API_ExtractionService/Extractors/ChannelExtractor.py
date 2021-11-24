


import json
import os
from queue import Queue
import time
import networkx
import random
from Youtube.API_ExtractionService.Extractors.helper import openURL

from .legacy.videos_channelid import channelVideo
from config import MAXDEMANDS, REGIONCODE, YOUTUBE_SEARCH_URL, YOUTUBE_TOKEN   # to become a context.. #one_of_the_somedays..


class ChannelExtractor:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def crawlChannel(graph,fullSchema,termQueue,videoQueue,channelQueue,playlistQueue,commentQueue,replyQueue):
        
        ChannelExtractor.fullStructure = fullSchema

        freshChannel = channelQueue.get()
        ChannelExtractor.insertUser(user=freshChannel,graph=graph)

        while True:
            # print("Abagain")
            
            sv = channelVideo(freshchannel, MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)           
            
            try:
            
                url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                nextPageToken = url_response.get("nextPageToken")
                sv.load_channel_videos(url_response)

                while nextPageToken:
                    sv.params.update({"pageToken": nextPageToken})
                    url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                    nextPageToken = url_response.get("nextPageToken")
                    sv.load_channel_videos(url_response)

                
                ChannelExtractor.scrapVideos(sv.videos,graph,videoQueue)
                
            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.with_traceback)

                #emptying the queue to channelinate the thread..
                while not channelQueue.empty():
                    
                    channelQueue.task_done()
                    
                    channelQueue.get()
                

            channelQueue.task_done()
            freshchannel = channelQueue.get()

    @staticmethod
    def insertChannel(args):
        pass

    @staticmethod
    def scrapVideos(vids,graph,videoQueue:Queue):
        for video in vids:
            if video["videoId"] not in graph: #just to put less noise in the queue
                videoQueue.add(video)
            print(video)
            
            
