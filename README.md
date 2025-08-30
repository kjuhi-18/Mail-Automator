📧 Image Mail Automator

Automate sending personalized image attachments effortlessly!
This Python tool sends different images to different recipients in one go. Each recipient gets one image (1.jpg, 2.jpg, …) mapped to their email address, with a common subject & body text. 🚀

✨ Features

✔️ Automated bulk sending – no manual effort

✔️ Unique image for each recipient (based on order)

✔️ Common subject & body – same for all recipients

✔️ Secure Gmail SMTP integration

✔️ Perfect for certificates, invitations, IDs, or QR codes


⚙️ How It Works

1️⃣ Store images as 1.jpg, 2.jpg, 3.jpg, … inside the images/ folder

2️⃣ Create an emails.txt file with recipients in the same order

3️⃣ Add your Gmail address & App Password to the script

4️⃣ Run the script → each recipient gets their corresponding image 📩

5️⃣ Done! 🎉

📌 Use Cases

🏆 Certificates – distribute event/contest certificates

🎟️ Invites – send unique QR-coded event invitations

🆔 ID Cards – bulk distribution to students/employees

💼 Reports/Receipts – automated personalized delivery

🚀 Quick Start
🔧 Requirements

Python 3.x

smtplib (built-in)

email (built-in)

🛠️ Gmail Setup (Important!)

To make this work, you need your Gmail + App Password:

Go to Google Account Security
.

Enable 2-Step Verification.

Generate an App Password (choose Mail → Windows Device).

Copy the 16-character password.

Open mail_automator.py and edit these lines:

SENDER_EMAIL = "yourgmail@gmail.com"

PASSWORD = "your-16-digit-app-password"

SUBJECT = "Your Subject Here"

BODY = "Hello,\n\nPlease find your attachment.\n\nBest Regards"

▶️ Run the Project
python mail_automator.py


✅ Each recipient in emails.txt will receive the corresponding image from the images/ folder.

📂 Project Structure
📦 Image-Mail-Automator
 ┣ 📜 mail_automator.py      # main script
 ┣ 📜 emails.txt             # recipient list (one email per line)
 ┣ 📂 images/                # 1.jpg, 2.jpg, ...
 ┗ 📜 README.md

🌟 Why Use This?

Sending 100+ personalized emails with attachments manually is boring & error-prone 😓.
This project makes it fast ⚡, reliable ✅, and hassle-free 🎉.

💡 Future Enhancements

✅ Support for HTML-rich body content
✅ Multiple attachments per recipient
✅ CSV-based email-image mapping

🔥 Save hours of manual effort – let automation handle your mailing!
