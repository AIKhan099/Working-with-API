import request
from pprint import pprint
url= "https://icanhazdadjoke.com

payload={}
headers={ "Accept":"application/json"}
response= requests.request("GET", url, headers=headers, data=payload)

responseJson=response.json()
pprint(responseJson)
print(response.text)
print("Your generated joke is :" + str(responseJson['joke']))
