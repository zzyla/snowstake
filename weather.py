# open meteo for getting current weather conditions based on lat long
# in the future we may switch this to a snow based service

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from destinations import destinations

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"

def getCurrentWeather(inputDestination):
    location  = destinations[inputDestination]
    params = {
        "latitude": location["lat"],
        "longitude": location["long"],
        "current": ["temperature_2m", "precipitation", "wind_speed_10m", "cloud_cover", "wind_direction_10m", "apparent_temperature", "snowfall"],
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch"
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation {response.Elevation()} m asl")
    # print(f"Timezone {response.Timezone()}{response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # get all of the desired current info
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_precipitation = current.Variables(1).Value()
    current_wind_speed_10m = current.Variables(2).Value()
    current_cloud_cover = current.Variables(3).Value()
    current_wind_direction_10m = current.Variables(4).Value()
    current_apparent_temperature = current.Variables(5).Value()
    current_snowfall = current.Variables(6).Value()
    
    # convert degrees to compass direction
    current_wind_direction_10m = degToCompass(current_wind_direction_10m)
    

    # print(f"Current time {current.Time()}")

    # print(f"Current temperature_2m {current_temperature_2m}")
    # print(f"Current precipitation {current_precipitation}")
    # print(f"Current wind_speed_10m {current_wind_speed_10m}")
    # print(f"Current cloud_cover {current_cloud_cover}")
    # print(f"Current wind_direction_10m {current_wind_direction_10m}")
    # print(f"Current apparent_temperature {current_apparent_temperature}")
    # print(f"Current snowfall {current_snowfall}")
    
    # output the results
    return f"""
            Current Temp: {current_temperature_2m}\n
            Current Feels Like Temp: {current_apparent_temperature}\n
            Current Snowfall: {current_snowfall}\n 
            Current Precip: {current_precipitation} \n 
            Current Wind Speed: {current_wind_speed_10m}\n
            Current Cloud Cover: {current_cloud_cover}\n 
            Current Wind Direction: {current_wind_direction_10m}\n
            """

# stack overflow convert - lets see if it work
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return (arr[(val % 16)])