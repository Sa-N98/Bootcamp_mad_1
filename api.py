from flask_restful import Resource
from model import *

  #CRUD
class demoAPI(Resource):

    def post(self):    # Adding or sending data to the back end or data base     C
        return
    
    def get(self):     # Retrice or get data from the data base or function      R
        return
    
    def put(self):     #  Edit data base                                         U
        return 
    
    def delete(self):  # Deletes                                                 D
        return 
    

class databaseAPI(Resource):

    def post(self ,num1, num2):
                                 # Adding or sending data to the back end or data base     C
        return int(num1)+int(num2)
    
    def get(self,):     # Retrice or get data from the data base or function      R
        
        first3Movie = movies.query.limit(3).all()
        jason ={}
        
        counter =0
        for items in first3Movie:

            jason['movie'+str(counter)] = [ items.id, items.title , items.rating]
            counter+=1

        return  jason
    
    def put(self):     #  Edit data base                                         U
        return  "YOY ARE IN PUT"
    
    def delete(self):  # Deletes                                                 D
        return  " OK WE GIR IT "
    