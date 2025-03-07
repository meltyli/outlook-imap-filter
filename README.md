### Outlook IMAP Email Filter  

A Python script that connects to an Outlook email account via IMAP and moves emails containing a specific keyword (e.g., "baby") to a designated folder.  

#### Features  
- Connects to Outlook via IMAP  
- Searches emails for a keyword in the subject or body  
- Moves matching emails to a specified folder  

#### Requirements  
- Python 3.x  
- `imapclient` (`pip install imapclient`)  

#### Setup & Usage  
1. Enable IMAP in your Outlook settings  
2. Install dependencies:  
   ```bash
   pip install imapclient
   ```  
3. Update the script with your Outlook credentials  
4. Run the script:  
   ```bash
   python filter_emails.py
   ```  

#### Security Tip  
For security, use an **App Password** instead of your regular Outlook password.  

---
