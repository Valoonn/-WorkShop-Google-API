import sys
sys.path.insert(1, '../../GoogleDrive')
from getCreds import getCred
from apiclient.http import MediaFileUpload

fileName = sys.argv[1]

drive_service = getCred()

file_metadata = { 'name' : fileName }
media = MediaFileUpload(fileName)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

print ('File ID: %s' % file.get('id'))