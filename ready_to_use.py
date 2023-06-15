import requests
import time

"""
# MailHog Configurations
"""
MAILHOG_API_BASE_URL = 'http://localhost:8025/api/v2'  # Update with your MailHog API URL
MAILHOG_API_1_BASE_URL = 'http://localhost:8025/api/v1'  # Update with your MailHog API URL
HOST = "localhost"
PORT = "2525"
EMAIL = "test@test.com"
RELEASING_JSON_CONFIGURATION = {"host": HOST, "port": PORT, "email": EMAIL}

"""
# Fetching all emails from the mailhog API
"""
def release_all_emails():
    url = f"{MAILHOG_API_BASE_URL}/messages"
    response = requests.get(url)
    if response.status_code == 200:
        emails = response.json().get('items', [])
        if len(emails) > 0:
            for email in emails:
                release_email(email['ID'])
        else:
            print("No Messages Left In MailHog.")
    else:
        print("Failed to retrieve emails from MailHog.")

"""
# Releasing the email to it's original destination through MAILHOG API and deleting the message after the release
"""
def release_email(email_id):
    print("connecting...")
    print("releasing......")
    release = requests.post(f"{MAILHOG_API_1_BASE_URL}/messages/{ email_id }/release", 
                  json=RELEASING_JSON_CONFIGURATION)
    print(release.status_code)
    if release.status_code == 200:
        print("deleting after releasing...")
        delete = requests.delete(f"{MAILHOG_API_1_BASE_URL}/messages/{ email_id }")
        print(delete.status_code)


# usage:
release_all_emails()
