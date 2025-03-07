import imaplib
import email
from imapclient import IMAPClient

# Outlook IMAP settings
IMAP_SERVER = "imap-mail.outlook.com"
EMAIL_ACCOUNT = "you-email@outlook.com"
email_PASSWORD = "your-password"

#Connect to Outlook IMAP
with IMAPClient(IMAP_SERVER) as client:
  client.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
  client.select_folder("INBOX", readonly=FALSE)

  # Search for emails containing "baby" in the subject or body
  messages = client.search(['BODY', 'baby']) # Searc entire email mode
  print(f"Found {len(messages)] emails with 'baby '")

  for msgid in messages:
        # Move to "Baby Stuff" folder (create it first in Outlook if it doesn't exist)
        client.move([msgid], "Baby Stuff")
        print(f"Moved email ID {msgid} to 'Baby Stuff'")

  client.logout()
