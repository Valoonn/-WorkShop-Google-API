import sys
sys.path.insert(1, '../../GoogleDrive')
from getCreds import getCred
from googleapiclient.discovery import build


def createEmptyFile (fileName) :
    drive_service = build('drive', 'v3', credentials=getCred())

    file_metadata = {
        'name' : fileName,
        'mimeType' : 'application/vnd.google-apps.drive-sdk'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print ('File ID: %s' % file.get('id'))