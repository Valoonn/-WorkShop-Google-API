import sys, json
from googleapiclient.discovery import build
from apiclient import errors
from lib import getCreds
from apiclient.http import MediaFileUpload

def uploadFile(filePath) :
    drive_service = build('drive', 'v3', credentials=getCreds.getCred())

    file_metadata = { 'name' : filePath }
    media = MediaFileUpload(filePath)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ('Successfully created file ID: "%s", name : "%s"' % (file.get('id'), filePath))
    return (file.get('id'))

def createFolder(folderName) :

    drive_service = build('drive', 'v3', credentials=getCreds.getCred())

    file_metadata = {
        'name': folderName,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

    print ('Successfully created folder ID: "%s", name : "%s"' % (folder.get('id'), folderName))
    return (folder.get('id'))


def deleteFolder(folderName) :

    ## Le nom du fichier est l'id que l'on trouve dans l'URL sur google drive

    ## https://drive.google.com/drive/folders/1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB
    ## ID = 1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB

    drive_service = build('drive', 'v3', credentials=getCreds.getCred())
    try:
        folder = drive_service.files().delete(fileId=folderName).execute()
    except errors.HttpError:
        print ('An error occurred')

