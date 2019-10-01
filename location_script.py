import urllib.request
import json

api_clientid = "KI1SKBADGX3VXXYHGOMNNLSMC0I5NXP0KMDLB1J3CUS1DOWJ"
api_clientScret = "WIBENCT2PDA0RTEP3NSMNPFUHZD4X4R3NQHIGMEX5KTCH51I"


print("Please select the following resturants:")
print("1. JJ Cafe")
print("2. Gus's World Famous Fried Chicken")
print("3. Left Coast Brewing")
print("4. Gen Korean BBQ House")

x = input("choice: ")

while(int(x) > 4 or int(x) < 1):
    if int(x) > 4 or int(x) < 1:
        print("Please select a number between 1 - 4.")
        x = input("choice: ")

if x == "1":
    location_long = -118.129001
    location_lat = 34.062657
elif x == "2":
    location_long = -118.302252
    location_lat = 34.179919
elif x == "3":
    location_long = -117.764073
    location_lat = 33.668146
elif x == "4":
    location_long = -118.127609
    location_lat = 34.094509

api_url = "https://api.foursquare.com/v2/venues/search?client_id=" + api_clientid + "&client_secret=" + api_clientScret + "&v=20181007&ll=" + str(location_lat) + "," + str(location_long) + "&limit=1"

obj = urllib.request.urlopen(api_url)

data = json.load(obj)

print("Location Name:" + data['response']['venues'][0]['name']) 
print("Location Address: " + data['response']['venues'][0]['location']['address'] + " " + data['response']['venues'][0]['location']['city'] + ", " + data['response']['venues'][0]['location']['state'] + " " + data['response']['venues'][0]['location']['postalCode'] +  ", " + data['response']['venues'][0]['location']['country'])
print("Category: " + data['response']['venues'][0]['categories'][0]['name'])
