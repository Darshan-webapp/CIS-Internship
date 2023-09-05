import requests, json 

city_name = input("Enter city name: ")
base_url = "https://whalewatchmaker.com/cis-weather?city="+city_name

response = requests.get(base_url)
x = response.json()
print("city: "+x["city"])
print("temperature: "+str(x["temperature"]))
print("humidity: "+str(x["humidity"]))
print("condition: "+x["condition"])

