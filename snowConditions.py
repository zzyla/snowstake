from destinations import destinations
import requests
# ski resort forecast API - rapid api 
# big yeah maybe this is really slow

headers = {
	"x-rapidapi-key": "f040484987msh489916c0fd8fd0dp1448b0jsn15150cec5c9f",
	"x-rapidapi-host": "ski-resort-forecast.p.rapidapi.com"
}
# querystring = {"region":"USA - Colorado"}
# url = "https://ski-resort-forecast.p.rapidapi.com/resorts"

destinationsCond = {
"Copper" : "Copper-Mountain",
"Winter Park (Mary Jane)" : "Winter-Park",
"Keystone" : "Keystone-Resort",
"Eldora" : "Eldora",
"Echo" : "EchoMountain",
"Loveland": "Loveland",
"Breckenridge" : "Breckenridge",
"Vail" : "Vail",
"Beaver Creek" : "Beaver-Creek",
"Arapahoe Basin" : "Arapahoe-Basin"
}

def getsnowConditions(inputDestination):
    destination  = destinationsCond[inputDestination]
    url = f"https://ski-resort-forecast.p.rapidapi.com/{destination}/snowConditions?units=i"


    # response = requests.get(url, headers=headers, params=querystring)
    response = requests.get(url, headers=headers)
    response = response.json()
    topSnowDepth = response["topSnowDepth"]
    botSnowDepth = response["botSnowDepth"]
    freshSnow = response["freshSnowfall"]
    lastSnow = response["lastSnowfallDate"]
    
    return f"""
            Top snow depth: {topSnowDepth} \n
            Bottom snow depth: {botSnowDepth} \n
            Fresh snow: {freshSnow} \n
            Last snow date: {lastSnow}
            """

def getForecast(inputDestination):
    destination  = destinationsCond[inputDestination]
    url = f"https://ski-resort-forecast.p.rapidapi.com/{destination}/forecast?units=i&el=top"

    response = requests.get(url, headers=headers)
    response = response.json()
    summaryThreeDay = response["summary3Day"]
    summarySixDay = response["summaryDays4To6"]
    
    
    return f"""
            3 day forecast: {summaryThreeDay} \n
            4 to 6 Day forecast: {summarySixDay} \n
        """