import smtplib
import ssl
from email.message import EmailMessage
import os
import re

sender_email = ""     # Your Gmail address
app_password = ""     # Your 16-character App Password (not Gmail password!)
subject = ""  # Email subject line
body_text = (
    "Hi,\n\n"
    ""#body text
    "Regards,\n"
    "\n"#sender name

)

# Paths
image_folder = ""        # Folder containing certificates
email_list_file = ""  # File with recipient emails
# -------------------------------------------------

# Step 1: Load recipient email addresses
with open(email_list_file, "r") as f:
    recipients = [line.strip() for line in f.readlines() if line.strip()]

# Step 2: Collect and sort image files (expects names like 1.jpg, 2.jpg, ...)
image_files = [
    f for f in os.listdir(image_folder)
    if re.fullmatch(r"\d+\.jpg", f, re.IGNORECASE)  # Only numeric .jpg files
]
image_files = sorted(image_files, key=lambda x: int(x.split('.')[0]))

# Step 3: Validate counts (must be equal: one image per email)
if len(recipients) != len(image_files):
    raise Exception(f"Mismatch: {len(recipients)} emails and {len(image_files)} images.")

# Step 4: Create secure SSL context for Gmail SMTP
context = ssl.create_default_context()

# Step 5: Send personalized emails
for i in range(len(recipients)):
    # Create email message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipients[i]
    msg.set_content(body_text)

    # Attach corresponding image (1st email -> 1.jpg, 2nd -> 2.jpg, etc.)
    image_path = os.path.join(image_folder, image_files[i])
    with open(image_path, "rb") as img:
        img_data = img.read()
        msg.add_attachment(img_data, maintype="image", subtype="jpeg", filename=image_files[i])

    # Connect to Gmail SMTP and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    # Log progress
    print(f"[✓] Sent to {recipients[i]} with image {image_files[i]}")
