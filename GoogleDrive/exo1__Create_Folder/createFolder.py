import sys
sys.path.insert(1, '../../GoogleDrive')
from getCreds import getCred
from googleapiclient.discovery import build


def createFolder(folderName) :

    drive_service = build('drive', 'v3', credentials=getCred())

    file_metadata = {
        'name': folderName,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

    print ('Folder ID: %s' % folder.get('id'))
