# Jira to Sheets

This project gathers issues from Jira—including ticket summary, ticket number, priority, and assignee—and compiles them into a Google Sheet. A new sheet is created with each import, making it easy to track issue snapshots over time.

A follow-up Google Apps Script (not yet included) can be used to format the document, making it easier to scan and interpret. Currently, all tickets are sorted by Epics, with the following order:

- Blocked
- In Progress
- Open

A row with a dash (`—`) is inserted between Epics for clarity and separation.

This tool is designed to give a high-level view of development progress. It’s especially useful for identifying new priority bugs, making project notes, or preparing data for use in a Gantt chart.

---

## 🔧 Technologies Used

- Python
- Jira REST API
- Google Sheets API
- Google Apps Script (optional, separate)

---

## 🚀 Usage

1. Set up your Jira and Google Sheets credentials.
2. (Optional) Create a `.env` file to store your API keys and configuration.
3. Run the script:

   ```bash
   python main.py
