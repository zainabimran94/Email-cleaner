from datetime import datetime, timedelta
import os.path
import time
from crontab import CronTab
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://mail.google.com/" 
]

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens
    # and is created automatically when the authorization flow completes.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES  # Change here
            )
            creds = flow.run_local_server(port=5500)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")
        for label in labels:
            print(label["name"])

     
        # Delete old emails
        delete_old_emails(service)

        # Delete unopened emails older than 3 days
        delete_unopened_emails(service)

    except HttpError as error:
        print(f"An error occurred: {error}")

def delete_old_emails(service):
    # Get emails older than July 1, 2024
    cutoff_date = '2024/09/30'
    result = service.users().messages().list(userId='me', q=f'before:{cutoff_date} label:Social OR label:Bin').execute()
    messages = result.get('messages', [])
    
    if not messages:
        print("No old emails found to delete.")
        return
    
    for msg in messages:
      service.users().messages().delete(userId='me', id=msg['id']).execute()
      print(f"Deleted email ID: {msg['id']}")
        
      time.sleep(1)

def delete_unopened_emails(service):
    # Get today's date and calculate cutoff date for unopened emails
    cutoff_date = (datetime.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    result = service.users().messages().list(userId='me', q=f'before:{cutoff_date}').execute()
    messages = result.get('messages', [])
    
    if not messages:
        print("No unopened emails found to delete.")
        return

    for message in messages:
        service.users().messages().delete(userId='me', id=message['id']).execute()
        print(f"Deleted unopened message ID: {message['id']}")


if __name__ == "__main__":
    main()

