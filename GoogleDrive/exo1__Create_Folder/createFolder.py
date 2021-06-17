import sys
sys.path.insert(1, '../../GoogleDrive')
from getCreds import getCred

folderName = sys.argv[1]

drive_service = getCred()

file_metadata = {
    'name': folderName,
    'mimeType': 'application/vnd.google-apps.folder'
}
folder = drive_service.files().create(body=file_metadata,
                                    fields='id').execute()

print ('Folder ID: %s' % folder.get('id'))