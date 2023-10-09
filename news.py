import requests 
from apikeys import news_key
api_address = "http://newsapi.org/v2/top-headlines?country=us&apiKey="+news_key
json_data = requests.get(api_address).json()



def news():
    ar = []
    for i in range(3):
        ar.append("Number " + str(i+1)+", " + json_data["articles"][i]["title"] + ".")
    
    return ar 

arr = news()

        
        
        