import sys
from lib import getCreds
from googleapiclient.discovery import build
import gspread

## Creer un dossier sur Google Drive et copier son ID ici
WORKSHOP_FOLDER_ID = "1wxsqHjFMJBB4UueMGFsiUzKpFk3cz2n_"

def createSheet(fileName, folderId = '') :

    drive_service = build('sheets', 'v4', credentials=getCreds.getCred())

    spreadsheet = {
        'properties': {
            'title': fileName,
        }
    }
    results = drive_service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()
    print ('Successfully created Spreadsheet ID: "%s", name : "%s"' % (results.get('spreadsheetId'), fileName))

    drive = build('drive', 'v3', credentials=getCreds.getCred())
    res = drive.files().update(fileId=results['spreadsheetId'], addParents=folderId, removeParents='root').execute()


def initSheet(sheet) :
    sheet.insert_row(["NOM DU RESTAURANT", "ADDRESSE", "OUVERT ?", "NOTE"], 1)


def fillWithData(info, sheet) :
    try :
        name = info["name"]
    except KeyError:
        ouvert = "N/A"
    try :
        address = info["formatted_address"]
    except KeyError:
        ouvert = "N/A"
    try :
        ouvert = str(info["opening_hours"]["open_now"])
    except KeyError:
        ouvert = "N/A"
    try :
        note = str(info["rating"]) + "/5"
    except KeyError:
        note = "N/A"

    sheet.insert_row([name, address,
                    ouvert, note], 2)


def openSheet(fileName) :
    client = gspread.authorize(getCreds.getCred())
    sheet = client.open(fileName).sheet1
    sheet.clear()
    initSheet(sheet)
    return (sheet)
