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

print(x)

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

print(api_url)



print(data)