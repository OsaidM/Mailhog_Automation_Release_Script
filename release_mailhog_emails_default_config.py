import requests
import time

MAILHOG_API_BASE_URL = 'http://localhost:8025/api/v2'  # Update with your MailHog API URL

def release_all_emails():
    url = f"{MAILHOG_API_BASE_URL}/messages"
    response = requests.get(url)
    if response.status_code == 200:
        emails = response.json().get('items', [])
        for email in emails:
            release_email(email['ID'])
    else:
        print("Failed to retrieve emails from MailHog.")

def release_email(email_id):
    url = f"{MAILHOG_API_BASE_URL}/messages/{email_id}/release"
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        print(f"Released email with ID: {email_id}")
    else:
        print(f"Failed to release email with ID: {email_id}")

# Example usage:
release_all_emails()
time.sleep(2)  # Wait for 2 seconds before releasing individual email
