import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_KEY")

# get direction data from denver to copper mountain
url = "https://routes.googleapis.com/directions/v2:computeRoutes"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key":GOOGLE_MAPS_KEY,
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline"
}

homeCords = {"lat": 39.76894267994319, "long": -105.05439923229812}
copperCords = {"lat": 39.50154207577621, "long": -106.15164399988696}

def getRoute():
    location  = copperCords
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
    
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    time = data["routes"][0]["duration"]
    time = time[:-1]
    time = convertTime(int(time))
        
    return time


def convertTime(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d hr %02d min %02d s' % (hour, min, sec)