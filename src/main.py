from src.email_parser import parse_email
from src.sheets_service import get_sheets_service, append_email
from config import SCOPES
from src.gmail_service import get_gmail_service, fetch_unread_emails
import json
import os

SPREADSHEET_ID = "1cIQIhU6tw40j2-1oGM1H8ib9iGQX2IfjE356MoX8mz0"
STATE_FILE = "state.json"  # to store processed email IDs

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"processed_ids": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main():
    # Authenticate Gmail & get credentials
    service, creds = get_gmail_service(SCOPES)

    # Authenticate Google Sheets
    sheets_service = get_sheets_service(creds)

    # Load processed email IDs
    state = load_state()
    processed_ids = set(state.get("processed_ids", []))

    # Fetch unread emails
    emails = fetch_unread_emails(service)
    print(f"Unread emails found: {len(emails)}")

    new_processed = []

    for msg in emails:
        if msg["id"] in processed_ids:
            continue  # skip already processed

        # Get full message to access payload
        full_msg = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        parsed_email = parse_email(full_msg)

        # Append to Google Sheet
        append_email(sheets_service, SPREADSHEET_ID, parsed_email)

        # Mark as read
        service.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        new_processed.append(msg["id"])

    # Update state
    processed_ids.update(new_processed)
    save_state({"processed_ids": list(processed_ids)})

    print(f"Processed {len(new_processed)} new emails.")

if __name__ == "__main__":
    main()

