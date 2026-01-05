import csv
import smtplib
import os
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "Bhakti Enterprises")


EMAIL_SUBJECT = "Your Trusted Partner for Copier Solutions & Spare Parts"


contacts_file = 'contactsmock.csv'
generated_emails_dir = Path('generated_emails')

def load_html_file(filename):
    """Load HTML content from generated email file"""
    filepath = generated_emails_dir / filename
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"[ERROR] File not found: {filename}")
        return None

def send_email(to_email, to_name, html_content, html_filename):
    """Send email with HTML content and HTML file as attachment"""
    try:
        # Use 'mixed' to support both HTML body and attachments
        msg = MIMEMultipart('mixed')
        msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        msg['To'] = to_email
        msg['Subject'] = EMAIL_SUBJECT
        
        # Create alternative part for HTML body
        html_body = MIMEMultipart('alternative')
        html_part = MIMEText(html_content, 'html', 'utf-8')
        html_body.attach(html_part)
        msg.attach(html_body)
        
        # Attach the HTML file
        filepath = generated_emails_dir / html_filename
        if filepath.exists():
            with open(filepath, 'rb') as f:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {html_filename}'
                )
                msg.attach(attachment)
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        return True, None
    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed. Check your email and password."
    except smtplib.SMTPRecipientsRefused:
        return False, f"Recipient email address invalid: {to_email}"
    except smtplib.SMTPServerDisconnected:
        return False, "Server disconnected. Check your SMTP settings."
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    print("=" * 60)
    print("Bhakti Enterprises - Email Sender")
    print("=" * 60)
    print()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("[ERROR] .env file not found!")
        print()
        print("Please create a .env file with the following variables:")
        print("  SENDER_EMAIL=your-email@gmail.com")
        print("  SENDER_PASSWORD=your-app-password")
        print("  SENDER_NAME=Your Name")
        print("  SMTP_SERVER=smtp.gmail.com")
        print("  SMTP_PORT=587")
        print()
        print("You can copy .env.example to .env and update the values.")
        print()
        return
    
    # Check if configuration is set
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("[ERROR] SENDER_EMAIL or SENDER_PASSWORD not set in .env file!")
        print()
        print("Please make sure your .env file contains:")
        print("  SENDER_EMAIL=your-email@gmail.com")
        print("  SENDER_PASSWORD=your-app-password")
        print()
        print("For Gmail:")
        print("1. Enable 2-Step Verification")
        print("2. Generate an App Password: https://myaccount.google.com/apppasswords")
        print("3. Use the app password (not your regular password)")
        print()
        return
    
    # Read contacts
    if not os.path.exists(contacts_file):
        print(f"[ERROR] Contacts file not found: {contacts_file}")
        return
    
    with open(contacts_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        contacts = list(reader)
    
    print(f"Found {len(contacts)} contacts to send emails to")
    print()
    
    # Track results
    success_count = 0
    failed_count = 0
    failed_contacts = []
    
    # Send emails
    for i, contact in enumerate(contacts, 1):
        name = contact['name']
        email = contact['email']
        filename = f"{name.replace(' ', '_')}_email.html"
        
        print(f"[{i}/{len(contacts)}] Sending to {name} ({email})...")
        
        # Load HTML content
        html_content = load_html_file(filename)
        if html_content is None:
            print(f"  [SKIPPED] Could not load HTML file: {filename}")
            failed_count += 1
            failed_contacts.append((name, email, "HTML file not found"))
            continue
        
        # Send email
        success, error_msg = send_email(email, name, html_content, filename)
        
        if success:
            print(f"  [SUCCESS] Email sent successfully!")
            success_count += 1
        else:
            print(f"  [FAILED] {error_msg}")
            failed_count += 1
            failed_contacts.append((name, email, error_msg))
        
        print()
    
    # Summary
    print("=" * 60)
    print("SENDING SUMMARY")
    print("=" * 60)
    print(f"Total contacts: {len(contacts)}")
    print(f"Successfully sent: {success_count}")
    print(f"Failed: {failed_count}")
    print()
    
    if failed_contacts:
        print("Failed contacts:")
        for name, email, error in failed_contacts:
            print(f"  - {name} ({email}): {error}")
        print()
    
    print(f"[COMPLETE] Email sending process finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()

