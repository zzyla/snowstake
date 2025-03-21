import requests
from dotenv import load_dotenv
import json
import os
from destinations import destinations

load_dotenv()
GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_KEY")

# get direction data from denver to copper mountain
url = "https://routes.googleapis.com/directions/v2:computeRoutes"

# google maps api header, static with the api key
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key":GOOGLE_MAPS_KEY,
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline"
}

# keeping this for now, hard coded into payload anyway
homeCords = {"lat": 39.76894267994319, "long": -105.05439923229812}

# this fucntion takes in one of the preset destinations, calls the google maps api, and returns the time to reach the destination 
def getRouteTime(inputDestination):
    # acess the destinations dict with the key from the destination paramater
    location  = destinations[inputDestination]
    
    # payload for google maps api, access the coords of the provided destinations, start location is where I live
    payload = {
    "origin": {"location": {"latLng": {"latitude": 39.76894267994319, "longitude": -105.05439923229812}}},
    "destination": {"location": {"latLng": {"latitude": location["lat"], "longitude": location["long"]}}},
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE",
    "computeAlternativeRoutes": False,
    "routeModifiers": {"avoidTolls": False, "avoidHighways": False, "avoidFerries": False},
    "languageCode": "en-US",
    "units": "IMPERIAL"
    }
    
    # call the api, and convert the data
    response = requests.post(url, json=payload, headers=headers) # get request from google maps, using post as sending info
    data = response.json() # convert the response to json 
    time = data["routes"][0]["duration"] # access first routes time field 
    time = time[:-1] # time is returned as such: 12s, removing the s to convert to int
    time = convertTime(int(time))
    return f"Time to: {time}"

# function to convert seconds to "normal" time
def convertTime(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d hr %02d min %02d s' % (hour, min, sec)