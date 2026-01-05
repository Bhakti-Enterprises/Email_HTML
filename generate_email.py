import csv
import os
from pathlib import Path

with open('./init_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

output_dir = Path('generated_emails')
output_dir.mkdir(exist_ok=True)

with open('contacts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    contacts = list(reader)

for contact in contacts:
    whatsapp_number = contact['whatsapp_number']
    contact_number = contact['whatsapp_number']
    contact_number = contact_number.replace('+91', '+91-')
    contact_name = contact['name']
    email_id = contact['email']
    
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text=Hello%20{contact_name.replace(' ', '%20')},%20I%20am%20interested%20in%20your%20products"
    

    customized_html = template.replace('{{WHATSAPP_NUMBER}}', whatsapp_number)
    customized_html = customized_html.replace('{{EMAIL}}', email_id)
    # customized_html = customized_html.replace('{{CONTACT_NAME}}', contact_name)
    customized_html = customized_html.replace('{{CONTACT_NUMBER}}', contact_number)
    
  
    filename = f"{contact_name.replace(' ', '_')}_email.html"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(customized_html)
    
    print(f"Generated: {filename}")

print(f"\n[SUCCESS] Generated {len(contacts)} email files in '{output_dir}' folder")