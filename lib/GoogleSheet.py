import sys
from getCreds import getCred
from googleapiclient.discovery import build

WORKSHOP_FOLDER_ID = "1wxsqHjFMJBB4UueMGFsiUzKpFk3cz2n_"

def createSheet(fileName) :

    drive_service = build('sheets', 'v4', credentials=getCred())

    spreadsheet = {
        'properties': {
            'title': fileName,
        }
    }
    results = drive_service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(results.get('spreadsheetId')))

    drive = build('drive', 'v3', credentials=getCred())
    res = drive.files().update(fileId=results['spreadsheetId'], addParents=WORKSHOP_FOLDER_ID, removeParents='root').execute()



def initSheet(sheet) :
    sheet.insert_row(["NOM DU RESTAURANT", "ADDRESSE", "OUVERT ?", "NOTE"], 1)


def fillWithData(resto, sheet) :
    name = resto["name"]
    address = resto["formatted_address"]
    try :
        ouvert = str(resto["opening_hours"]["open_now"])
    except KeyError:
        ouvert = "N/A"
    try :
        note = str(resto["rating"]) + "/5"
    except KeyError:
        note = "N/A"

    sheet.insert_row([name, address,
                    ouvert, note], 2)


def fillSheet(style, address) :
    fileName = getPlace(style, address)
    jsonFile = open(fileName + ".json", "r")
    jsonFile = json.loads(jsonFile.read())
    createSheet(fileName)
    client = gspread.authorize(getCred())
    sheet = client.open(fileName).sheet1
    sheet.clear()
    initSheet(sheet)
    for address in jsonFile["results"]:
        fillWithData(address, sheet)
