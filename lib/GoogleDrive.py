import sys
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




def createFolder(folderName) :

    drive_service = build('drive', 'v3', credentials=getCred())

    file_metadata = {
        'name': folderName,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

    print ('Folder ID: %s' % folder.get('id'))




def deleteFolder(folderName) :

    ## Le nom du fichier est l'id que l'on trouve dans l'URL sur google drive

    ## https://drive.google.com/drive/folders/1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB
    ## ID = 1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB

    drive_service = build('drive', 'v3', credentials=getCred())
    drive_service.files().delete(fileId=folderName).execute()

