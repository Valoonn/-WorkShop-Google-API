import googlemaps, sys, json

apiKey = "AIzaSyDKlQi_AxBDLHbUr6fB3Din_5RjLF2LP_w"
exportPath = "./export/"


def getCoords(adress) :
    gmaps = googlemaps.Client(key=apiKey)
    results = gmaps.geocode(adress)
    return (results[0]['geometry']['location'])


def getPlace(style, coords, geo) :
    fileName = style + "(" + coords + ")"
    gmaps = googlemaps.Client(key=apiKey)
    print ("Extract all the place (style : '" + style + "') arround : '" + coords + "'")
    jsonSave = open(exportPath + fileName + ".json", "w")
    print ("file : '"+ fileName + "'")
    results = gmaps.places(style, location = geo, language = 'fr', radius=1)
    jsonSave.write (json.dumps(results, indent = 4, ensure_ascii = False))
    return (fileName)
