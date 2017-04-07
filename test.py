import requests
import json

print("Hello")
teststr = "Allan"

for character in teststr:
    print(character)

kermitdict = {'test' : "Helllos", 'test1' : "Hello2"}

print(kermitdict)
print(type(kermitdict))
resp = requests.get("https://frekvens.erhvervsstyrelsen.dk/findKanalerAPI.php?output=JSON&language=da&northings=6180000&eastings=714400")

print(resp.status_code)

json_output = resp.json()

print(json_output["results"][0]["frequencyAreas"][1][1])
