from googleapiclient.discovery import build

def get_sheets_service(creds):
    return build("sheets", "v4", credentials=creds)

def append_email(sheet_service, spreadsheet_id, email_data):
    values = [[
        email_data["from"],
        email_data["subject"],
        email_data["date"],
        email_data["body"]
    ]]

    body = {"values": values}

    sheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:D",
        valueInputOption="RAW",
        body=body
    ).execute()
