import sys, gspread, json
sys.path.insert(1, '../../GoogleDrive')
sys.path.insert(1, '../../GoogleSheet/ex01__Create_Sheet')
sys.path.insert(1, '../../GoogleMaps/ex2__Get_Places')
from getPlace import getPlace
from getCreds import getCred
from createSheet import createSheet
from googleapiclient.discovery import build

def initSheet(sheet) :
    sheet.insert_row(["NOM DU RESTAURANT", "ADDRESSE", "OUVERT ?", "PHOTO", "NOTE"], 1)

def fillWithData(resto, sheet) :
    name = resto["name"]
    address = resto["formatted_address"]
    try :
        ouvert = str(resto["opening_hours"]["open_now"])
    except KeyError:
        ouvert = ""
    try :
        photo = resto["photos"][0]["html_attributions"][0]
    except KeyError:
        photo = ""
    note = str(resto["rating"]) + "/5"

    sheet.insert_row([name, address,
                    ouvert, photo,
                    note], 2)

def fillSheet(style, address) :
    fileName = getPlace(style, address)
    jsonFile = open(fileName, "r")
    jsonFile = json.loads(jsonFile.read())
    createSheet(fileName)
    client = gspread.authorize(getCred())
    sheet = client.open(fileName).sheet1
    sheet.clear()
    initSheet(sheet)
    for address in jsonFile["results"]:
        fillWithData(address, sheet)
    # print (json.dumps(jsonFile["results"], indent = 4))

fillSheet(sys.argv[1], sys.argv[2])
