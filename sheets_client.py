import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets scopes
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate using your JSON credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("jiraToSheetsCredentials.json", scope)
client = gspread.authorize(creds)

# Open the main spreadsheet
spreadsheet = client.open("Jira Sync")

# Create a new worksheet with timestamp in MMDD-HHMM format
timestamp = datetime.now().strftime("%m%d-%H%M")
worksheet_title = f"Sync {timestamp}"
sheet = spreadsheet.add_worksheet(title=worksheet_title, rows="100", cols="10")

# Buffer to accumulate rows before batch writing
buffer = []

def prepare_sheet():
    """
    Add the header and a visual separator row.
    """
    global buffer
    buffer = []
    sheet.append_row(["Summary", "Ticket Number", "Assignee", "Status", "Priority", "Story Points"])
    sheet.append_row(["—", "", "", "", "", ""])

def append_epic_row(summary, key):
    buffer.append([summary, key, "", "", "", ""])

def append_ticket_row(summary, key, assignee, status, priority, story_points):
    buffer.append([summary, key, assignee, status, priority, story_points])

def insert_blank_row():
    buffer.append(["—", "", "", "", "", ""])

def flush_rows():
    if buffer:
        sheet.append_rows(buffer, value_input_option="USER_ENTERED")
