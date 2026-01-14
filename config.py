# config.py

# Google API scopes
GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]

SHEETS_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# Combined scopes
SCOPES = GMAIL_SCOPES + SHEETS_SCOPES

# Google Sheet configuration
SPREADSHEET_ID = "PASTE_YOUR_SHEET_ID_HERE"
SHEET_RANGE = "Sheet1!A:D"

# State file to prevent duplicates
STATE_FILE = "state.json"
