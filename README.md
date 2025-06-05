[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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

---

## 🧾 Google Sheets Formatting Script (Optional)

This repository includes an optional Google Apps Script file: `google_formatting.gs`.

After running the main Python script and creating a new tab in your Google Sheet, you can use this script to:

- Apply formatting for better readability
- Add bold headers, auto-fit columns, and color-code priority levels
- Visually group issues by Epic using dashed rows

### 🔧 How to Use It

1. Open your Google Sheet
2. Click `Extensions → Apps Script`
3. Copy the contents of `google_formatting.gs` into the script editor
4. Save and run the function (e.g., `formatSheetAndTrimAssignees`)
5. Accept permissions if prompted

This script is optional but useful if you’re sharing the sheet with stakeholders or using it to review tickets at a glance.
