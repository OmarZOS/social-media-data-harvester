


import json
import os
from queue import Queue
import time
import networkx
import random
from Youtube.API_ExtractionService.Extractors.helper import openURL

from Youtube.API_ExtractionService.Extractors.search_keyword import searchVideo
from config import MAXDEMANDS, REGIONCODE, YOUTUBE_SEARCH_URL, YOUTUBE_TOKEN   # to become a context.. #one_of_the_somedays..


class termSeeker:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def searchTerm(graph,fullSchema,termQueue,videoQueue,channelQueue,playlistQueue,commentQueue,replyQueue):
        
        termSeeker.fullStructure = fullSchema

        freshTerm = termQueue.get()
        # termSeeker.insertUser(user=freshUser,graph=graph)

        while True:
            # print("Abagain")
            
            sv = searchVideo(freshTerm, MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)
            
            try:
            
                url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                nextPageToken = url_response.get("nextPageToken")
                sv.load_search_res(url_response)

                while nextPageToken:
                    sv.params.update({"pageToken": nextPageToken})
                    url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                    nextPageToken = url_response.get("nextPageToken")
                    sv.load_search_res(url_response)
                
                termSeeker.scrapVideos(sv.videos,graph,videoQueue)
                termSeeker.scrapChannels(sv.channels,graph,channelQueue)
                termSeeker.scrapPlaylists(sv.playlists,graph,playlistQueue)
                


            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.with_traceback)

                #emptying the queue to terminate the thread..
                while not termQueue.empty():
                    
                    termQueue.task_done()
                    
                    termQueue.get()
                

            termQueue.task_done()
            freshTerm = termQueue.get()

    @staticmethod
    def scrapChannels(channels,graph,channelQueue):
        for channel in channels:
            if channel["channelId"] in graph: 
                continue
            channelQueue.add(channel)
            print(channel)
            

    @staticmethod
    def scrapPlaylists(playlists,graph,playlistQueue):
        for playlist in playlists:
            if playlist["playlistId"] in graph: 
                continue
            playlistQueue.add(playlist)
            print(playlist)


    @staticmethod
    def scrapVideos(vids,graph,videoQueue:Queue):
        for video in vids:
            if video["videoId"] in graph: #just to put less noise in the queue
                continue
            videoQueue.add(video)
            print(video)
