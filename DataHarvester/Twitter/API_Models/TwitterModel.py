from API_Models.API_ExtractionModel import API_extractionModel
import json

class TwitterModel(API_extractionModel):

    with open("Twitter/API_Models/TwitterSchema.json") as f:
        dataModel = json.load(f)


    def receiveData(self,ch,method,properties,body):
        print(body)

    def requestByModel(fields):
        pass
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

    

        
    