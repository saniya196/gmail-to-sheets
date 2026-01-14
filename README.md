
# Gmail to Google Sheets Automation

**Name:** Saniya Asreen

## Project Overview
This project is a Python automation system that reads real unread emails from my Gmail inbox and logs them into a Google Sheet. It uses the **Gmail API** to fetch emails and the **Google Sheets API** to store the data. Each email is added only once, and processed emails are marked as read.

---

## High-Level Architecture

```

+-------------------+
|   Gmail Inbox    |
| (Unread Emails)  |
+---------+---------+
|
v
+-------------------+
|  Gmail API (OAuth)|
+---------+---------+
|
v
+-------------------+
| Python Script     |
| - main.py         |
| - gmail_service.py|
| - email_parser.py |
| - sheets_service.py
+---------+---------+
|
v
+-------------------+
| Google Sheets API |
| (Append rows)     |
+-------------------+

````

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-github-repo-link>
cd gmail-to-sheets
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Enable APIs in Google Cloud Console

Enable:

* Gmail API
* Google Sheets API

### 4. OAuth Setup

1. Create an **OAuth Client ID** (Desktop Application)
2. Download `credentials.json`
3. Place it inside:

```
credentials/credentials.json
```

> Do NOT commit this file.

### 5. Run the script

```bash
python -m src.main
```

The first run will open a browser window for OAuth consent.

---

## OAuth Flow Used

This project uses **OAuth 2.0 (User Consent Flow)**:

* User authorizes Gmail and Sheets access
* Access token is stored locally
* No passwords or API keys are hardcoded
* Fully compliant with Google security guidelines

---

## Duplicate Prevention Logic

* Each Gmail message has a unique **message ID**
* Processed message IDs are saved in `state.json`
* Before processing an email, the script checks this file
* If the ID already exists, the email is skipped

This ensures **no duplicate rows** in Google Sheets.

---

## State Persistence Method

State is stored in a file called `state.json`.

Example:

```json
{
  "processed_ids": [
    "18c7a1f2a9b12345",
    "18c7a1f2a9b67890"
  ]
}
```

**Why this approach?**

* Lightweight and simple
* No database required
* Reliable for small to medium email volumes
* Ensures idempotent script execution

---

## Challenges Faced & Solutions

**Challenge:**
Encountered `KeyError: 'payload'` while parsing emails.

**Solution:**
Understood that `messages().list()` returns only message IDs.
Solved it by fetching full email content using:

```python
messages().get(format="full")
```

---

## Limitations

* Only processes **Inbox + Unread** emails
* Attachments are not handled
* Email body is stored as plain text only

---

## Bonus Features Implemented

* Emails are marked as **read** after processing
* Duplicate prevention using state persistence

---

## Proof of Execution

Screenshots and video are available in the `/proof/` folder:

* Gmail inbox with unread emails
* Google Sheet populated with at least 5 rows
* OAuth consent screen
* Screen recording explaining project flow

---

## Security Notes

The following files are NOT committed:

* `credentials.json`
* `token.json`

These are included in `.gitignore`.

---
📹 Screen Recording:
Google Drive Link: https://drive.google.com/file/d/10Ny4Pg_FiZ_PfoguEQuMO5bDXCf3hxWC/view?usp=sharing
