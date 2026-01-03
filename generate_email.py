import csv
import os
from pathlib import Path

# Read the template
with open('./init_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Create output directory
output_dir = Path('generated_emails')
output_dir.mkdir(exist_ok=True)

# Read contacts from CSV
with open('contacts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    contacts = list(reader)

# Generate HTML file for each contact
for contact in contacts:
    whatsapp_number = contact['whatsapp_number']
    contact_name = contact['name']
    
    # WhatsApp URL format: https://wa.me/919820229230?text=Hello
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text=Hello%20{contact_name.replace(' ', '%20')},%20I%20am%20interested%20in%20your%20products"
    
    # Replace placeholders
    customized_html = template.replace('{{WHATSAPP_NUMBER}}', whatsapp_number)
    customized_html = customized_html.replace('{{WHATSAPP_URL}}', whatsapp_url)
    customized_html = customized_html.replace('{{CONTACT_NAME}}', contact_name)
    
    # Save to file
    filename = f"{contact_name.replace(' ', '_')}_email.html"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(customized_html)
    
    print(f"Generated: {filename}")

print(f"\n[SUCCESS] Generated {len(contacts)} email files in '{output_dir}' folder")