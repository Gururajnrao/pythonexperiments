# we have imported the requests module 
import requests 
import json
# defined a URL variable that we will be 
# using to send GET or POST requests to the API 

class snowtooth:
  def __init__(self, url, json):
   self.url=url
   self.json=json
  
  def gqlresponse(self):
         
    self.response = requests.post(url=self.url, json=self.json) 
    print("response status code: ", self.response.status_code) 
    if self.response.status_code == 200: 
      print("response : ", self.response.content)
    return self.response.content
   
if __name__ == "__main__":
	  
  url = "https://snowtooth.moonhighway.com/"
  body = """
    { 
    allLifts {
    id
    name
    status
    }
    }

    """
  obj = snowtooth (url, json={"query":body})
  output=obj.gqlresponse()
  #print(output)
  jsonobj=json.loads(output)
  for lift in jsonobj['data']:
      print (lift['allLifts'][0])
    #print(jsonobj['data']['allLifts']['name'])
    #print(obj.url, obj.json)
		

