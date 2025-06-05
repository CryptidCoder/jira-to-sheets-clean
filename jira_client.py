import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env
load_dotenv()

# Jira credentials and site URL from .env
JIRA_SITE = os.getenv("JIRA_SITE")
EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")

# Authentication and headers for Jira API requests
JIRA_AUTH = HTTPBasicAuth(EMAIL, API_TOKEN)
JIRA_HEADERS = {
    "Accept": "application/json"
}

# Define the actual custom field ID for Story Points
STORY_POINTS_FIELD = "customfield_10028"

def get_issues_for_epic(epic_key, milestone=None):
    """
    Fetch issues from Jira associated with the given epic key.
    Optionally filter by milestone (custom field).
    """
    jql = f'"Epic Link" = {epic_key} AND status in ("Open", "In Progress", "In QA", "Blocked")'
    if milestone:
        jql += f' AND "Milestone[Dropdown]" = "{milestone}"'

    params = {
        "jql": jql,
        "fields": f"summary,status,assignee,priority,{STORY_POINTS_FIELD}",
        "maxResults": 50
    }

    response = requests.get(
        f"{JIRA_SITE}/rest/api/3/search",
        headers=JIRA_HEADERS,
        auth=JIRA_AUTH,
        params=params
    )

    if response.status_code == 200:
        return response.json().get("issues", [])
    else:
        print(f"❌ Failed to fetch issues for {epic_key}")
        print("Status code:", response.status_code)
        print("Response:", response.text)
        return []

def get_epic_summary(epic_key):
    """
    Fetch the summary (title) of the Epic from Jira using its issue key.
    """
    url = f"{JIRA_SITE}/rest/api/3/issue/{epic_key}"

    response = requests.get(
        url,
        headers=JIRA_HEADERS,
        auth=JIRA_AUTH
    )

    if response.status_code == 200:
        return response.json()["fields"]["summary"]
    else:
        print(f"❌ Failed to fetch epic summary for {epic_key}")
        print("Status code:", response.status_code)
        print("Response:", response.text)
        return "Unknown Epic"
