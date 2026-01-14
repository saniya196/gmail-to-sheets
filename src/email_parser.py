import base64
from email import message_from_bytes
def get_plain_text_body(payload):
    body = ""

    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain" and "data" in part["body"]:
                data = part["body"]["data"]
                body = base64.urlsafe_b64decode(data).decode("utf-8")
                break
    else:
        if payload["mimeType"] == "text/plain":
            data = payload["body"].get("data", "")
            body = base64.urlsafe_b64decode(data).decode("utf-8")

    return body.strip()
def parse_email(message):
    headers = message["payload"]["headers"]
    payload = message["payload"]

    email_data = {
        "from": "",
        "subject": "",
        "date": "",
        "body": ""
    }

    for header in headers:
        name = header["name"].lower()
        if name == "from":
            email_data["from"] = header["value"]
        elif name == "subject":
            email_data["subject"] = header["value"]
        elif name == "date":
            email_data["date"] = header["value"]

    email_data["body"] = get_plain_text_body(payload)

    return email_data
