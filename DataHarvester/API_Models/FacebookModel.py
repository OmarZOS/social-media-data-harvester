from API_ExtractionService.API_ExtractionModel import API_extractionModel


class FacebookModel(API_extractionModel):
    dataModel ={    "name": 'user', 
                    "cols":  {
                    "Bday": "int", 
                    "gender": "cid"}
                }

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

    

        
    