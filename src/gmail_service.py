import os
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
def get_gmail_service(scopes):
    creds = None

    # Load existing token if available
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)

    # If no valid credentials, perform OAuth login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/credentials.json", scopes
            )
            creds = flow.run_local_server(port=0)

        # Save token for future runs
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Build Gmail service
    service = build("gmail", "v1", credentials=creds)
    return service,creds
def fetch_unread_emails(service, max_results=10):
    response = service.users().messages().list(
        userId="me",
        labelIds=["INBOX", "UNREAD"],
        maxResults=max_results
    ).execute()

    messages = response.get("messages", [])
    return messages
def mark_email_as_read(service, message_id):
    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={"removeLabelIds": ["UNREAD"]}
    ).execute()
