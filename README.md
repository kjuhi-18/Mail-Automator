📧 Image Mail Automator

Automate sending personalized image attachments effortlessly!
This Python tool sends different images to different recipients in one go. Each recipient gets one image (1.jpg, 2.jpg, …) mapped to their email address, with a common subject & body text. 🚀

✨ Features

✔️ Automated bulk sending – no manual effort.


✔️ Unique image for each recipient (based on order).


✔️ Custom subject & body – same for all recipients.


✔️ SMTP integration for smooth email delivery.


✔️ Ideal for certificates, invitations, IDs, or QR codes.



⚙️ How It Works

1️⃣ Store images as 1.jpg, 2.jpg, 3.jpg, …


2️⃣ Prepare an email list in the same order.


3️⃣ Run the script → each recipient receives their corresponding image.


4️⃣ Done! 🎉



📌 Use Cases

🏆 Certificates – distribute event/contest certificates.

🎟️ Invites – send unique QR-coded event invitations.

🆔 ID Cards – bulk distribution to students/employees.

💼 Receipts/Reports – automated personalized delivery.

🚀 Quick Start
🔧 Requirements

Python 3.x

smtplib (built-in)

email (built-in)

▶️ Run the Project


python mail_automator.py


📂 Project Structure

📦 Image-Mail-Automator


 ┣ 📜 mail_automator.py
 
 ┣ 📜 emails.txt        # recipient list
 
 ┣ 📂 images/           # 1.jpg, 2.jpg, ...
 
 ┗ 📜 README.md

 

🌟 Why Use This?


Sending 100+ personalized emails with attachments manually is boring & error-prone 😓.
This project makes it fast, reliable, and hassle-free ⚡.

💡 Future Enhancements

✅ Support for HTML-rich body content

✅ Multiple attachments per recipient

✅ CSV-based email-image mapping

🔥 Save hours of manual effort – let automation handle your mailing!
