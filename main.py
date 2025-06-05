from jira_client import get_issues_for_epic, get_epic_summary
from sheets_client import prepare_sheet, append_epic_row, append_ticket_row, insert_blank_row, flush_rows

# 🔄 Start fresh
prepare_sheet()

# 🔐 Epic keys to check
epic_keys = [
    "REMT-4780", "REMT-6801", "REMT-8", "REMT-16", "REMT-14", "REMT-18", "REMT-25", "REMT-10",
    "REMT-6656", "REMT-18", "REMT-19", "REMT-20", "REMT-21", "REMT-12", "REMT-15", "REMT-24",
    "REMT-4069", "REMT-22", "REMT-23", "REMT-11"
]

# 🧩 Status priority order for sorting
STATUS_ORDER = {
    "In QA": 0,
    "Blocked": 1,
    "In Progress": 2,
    "Open": 3
}

for epic_key in epic_keys:
    print(f"🔍 Fetching tickets for {epic_key}...")
    issues = get_issues_for_epic(epic_key, milestone="RR_DEMO2")

    if not issues:
        continue

    # 🗂️ Sort by custom status order
    issues.sort(key=lambda issue: STATUS_ORDER.get(issue["fields"]["status"]["name"], 999))

    epic_summary = get_epic_summary(epic_key)
    append_epic_row(epic_summary, epic_key)

    for issue in issues:
        fields = issue["fields"]
        summary = fields.get("summary", "")
        key = issue.get("key", "")

        assignee_field = fields.get("assignee")
        assignee = assignee_field.get("displayName") if assignee_field else ""

        status = fields.get("status", {}).get("name", "")

        priority_field = fields.get("priority")
        priority = priority_field.get("name") if priority_field and priority_field.get("name") != "Not Set" else ""

        story_points = fields.get("customfield_10028", "")  # Actual Story Points field

        append_ticket_row(summary, key, assignee, status, priority, story_points)

    insert_blank_row()

insert_blank_row()  # Final extra space at the end

# 🚀 Push all buffered rows at once to avoid rate limit errors
flush_rows()

print("✅ Google Sheet updated successfully!")
