import requests, json 

city_name = input("Enter city name: ")
base_url = "https://whalewatchmaker.com/cis-weather?city="+city_name

response = requests.get(base_url)
x = response.json()

try:
    print("city: "+x["city"])
except:
    print("city not found")
try:
    print("gravity: "+x["gravity"])
except:
    print("not found")
try:
    print("temperature: "+str(x["temperature"]))
except:
    print("error")
try:
    print("humidity: "+str(x["humidity"]))
except:
    print("error")
try:
    print("condition: "+x["condition"])
except:
    print("something went wrong")