import os
from dotenv import load_dotenv

load_dotenv()

JIRA_SITE = os.getenv("JIRA_SITE")
EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")
SHEET_NAME = os.getenv("SHEET_NAME", "Jira Sync")
CREDENTIALS_FILE = "jiraToSheetsCredentials.json"  # or use a subfolder if you want
