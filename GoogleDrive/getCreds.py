from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']
PATH_TO_CRED = '../../credentials.json'
PATH_TO_TOKEN = '../token.json'

def getCred() :
    creds = None
    if os.path.exists(PATH_TO_TOKEN):
        creds = Credentials.from_authorized_user_file(PATH_TO_TOKEN, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../../credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(PATH_TO_TOKEN, 'w') as token:
            token.write(creds.to_json())
        creds = Credentials.from_authorized_user_file(PATH_TO_TOKEN, SCOPES)
    return (build('drive', 'v3', credentials=creds));