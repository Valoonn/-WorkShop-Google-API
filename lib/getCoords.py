import googlemaps, sys

apiKey = "AIzaSyDKlQi_AxBDLHbUr6fB3Din_5RjLF2LP_w"

def getCoords(adress) :
    gmaps = googlemaps.Client(key=apiKey)
    results = gmaps.geocode(adress)
    return (results[0]['geometry']['location'])
