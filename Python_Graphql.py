# we have imported the requests module 
import requests 
# defined a URL variable that we will be 
# using to send GET or POST requests to the API 
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

response = requests.post(url=url, json={"query": body}) 
print("response status code: ", response.status_code) 
if response.status_code == 200: 
	print("response : ", response.content) 
