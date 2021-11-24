from API_Models.API_ExtractionModel import API_extractionModel
import json

class YoutubeModel(API_extractionModel):

    # def __init__(self,*args):
        
        # if len(args)>1:
    with open("Youtube/API_Models/YoutubeSchema.json") as f:
        __dataModel = json.load(f)
        print(__dataModel.keys())
            
        


    def receiveData(self,ch,method,properties,body):
        print(body)

    def requestByModel(fields):
        pass

    def dataModel(self):
        return self.__dataModel;
        

    #  {
    #     [   
    #         name
    #         "user" :{
    #             [

    #         ]} 
    #         "userName" : "",
    #         "gender" : "",
    #         "location" : "",
    #     ]
    # }

    

        
    