# Email Cleanup Tool

This Python application utilizes the Gmail API to automate the deletion of emails. It deletes emails from a specific date and removes unread emails that have been in the inbox for more than a week. The tool is designed to help manage your inbox by automatically cleaning up old and unwanted emails.

## Features

- **Delete Emails by Date**: Removes emails older than a specified cutoff date.
- **Delete Unread Emails**: Automatically deletes unread emails that are older than seven days.
- **Gmail API Integration**: Utilizes Google's Gmail API for accessing and managing your email.
- **Automation**: Can be configured to run automatically using CronTab (on Unix-like systems).

## Requirements

- Python 3.6 or higher
- `google-auth`, `google-auth-oauthlib`, and `google-api-python-client` libraries
- Access to a Gmail account for API interaction
- `crontab` for scheduling (optional)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zainabimran94/Email-cleaner.git
   cd python
2. **Install dependencies: You can install the required libraries using pip:**
   pip install --upgrade google-auth google-auth-oauthlib google-api-python-client
3. **Set Up Google API Credentials:**
   1: Go to the Google Cloud Console.
   2: Create a new project and enable the Gmail API.
   3: Create OAuth 2.0 credentials and download the client_secret.json file.
   4: Place the client_secret.json file in the same directory as your script.
4. **Run the Application:**
   python3 hello.py

## Usage
1: The script will automatically delete emails before the specified cutoff date and remove unread emails older than seven days.
2: Customize the cutoff_date in the delete_old_emails function to change the threshold for deleting old emails.


