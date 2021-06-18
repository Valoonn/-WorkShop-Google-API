import googlemaps, json, sys
sys.path.insert(1, '../../GoogleMaps/ex1__Get_Coords')
sys.path.insert(1, '../../GoogleSheet/ex01__Create_Sheet')
import getCoords as co

apiKey = "AIzaSyDKlQi_AxBDLHbUr6fB3Din_5RjLF2LP_w"

def getPlace(style, coords) :
    fileName = style + "(" + coords + ").json"
    gmaps = googlemaps.Client(key=apiKey)
    print ("Extract all the place (style : '" + style + "') arround : '" + coords + "'")
    jsonSave = open(fileName, "w")
    print ("file : '"+ fileName + "'")
    results = gmaps.places(style, location = co.getCoords(coords), language = 'fr')
    jsonSave.write (json.dumps(results, indent = 4, ensure_ascii = False))
    return (fileName)
