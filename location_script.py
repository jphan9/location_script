import urllib.request
import json

api_clientid = "KI1SKBADGX3VXXYHGOMNNLSMC0I5NXP0KMDLB1J3CUS1DOWJ"
api_clientScret = "WIBENCT2PDA0RTEP3NSMNPFUHZD4X4R3NQHIGMEX5KTCH51I"
location_long = -118.4156806
location_lat = 34.564255
api_url = "https://api.foursquare.com/v2/venues/search?client_id=" + api_clientid + "&client_secret=" + api_clientScret + "&v=20181007&ll=" + str(location_lat) + "," + str(location_long) + "&limit=3"

obj = urllib.request.urlopen(api_url)

data = json.load(obj)



print(data)