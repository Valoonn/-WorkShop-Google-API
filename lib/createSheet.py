import sys
sys.path.insert(1, '../../GoogleDrive')
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
