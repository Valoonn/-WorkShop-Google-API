import sys
sys.path.insert(1, '../../GoogleDrive')
from getCreds import getCred
from googleapiclient.discovery import build

## Le nom du fichier est l'id que l'on trouve dans l'URL sur google drive

## https://drive.google.com/drive/folders/1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB
## ID = 1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB

def deleteFolder(folderName) :
    drive_service = build('drive', 'v3', credentials=getCred())
    drive_service.files().delete(fileId=folderName).execute()