from lib import GoogleDrive
from lib import GoogleSheet
from lib import GoogleMaps
import sys, json

exportPath = "./export/"

jsonFile = GoogleMaps.getPlace("restaurant", "95 rue de boissy, 95320",  GoogleMaps.getCoords("95 rue de boissy, 95320"))
GoogleSheet.createSheet(jsonFile, GoogleDrive.createFolder("workshop"))
sheet = GoogleSheet.openSheet(jsonFile)
jsonFile = open(exportPath + jsonFile + ".json", "r")
jsonFile = json.loads(jsonFile.read())
GoogleSheet.fillWithData(jsonFile["results"][0], sheet)