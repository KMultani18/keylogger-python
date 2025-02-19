Keylogger Project

🚀 About This Project
This project is a keylogger designed for educational and ethical security testing. It logs keystrokes, encrypts the log file, and sends the log to an email address.

⚠️ Disclaimer: This project is for educational and ethical use only. Unauthorized use of keyloggers is illegal in many jurisdictions.

📌 Features
✅ Logs all keystrokes, including timestamps.
✅ Encrypts keylog data before storing.
✅ Sends logs via email after a threshold of keystrokes or time.
✅ Uses environment variables to secure credentials.
✅ Supports exception handling and error logging.

🛠️ Installation & Setup

1️⃣ Prerequisites
Python 3.x installed
pip installed
A Gmail account (or another SMTP-compatible email service)

2️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME

3️⃣ Set Up Environment Variables
Create a .env file in the project root and add:

SENDER_EMAIL="your-email@gmail.com"
EMAIL_PASSWORD="your-app-password"
RECEIVER_EMAIL="receiver-email@gmail.com"


💡 Important: Use a Google App Password instead of your real email password. Learn More

🏃‍♂️ Running the Keylogger
python keylogger.py
The script will start logging keystrokes and send logs via email every 50 keystrokes or 5 minutes.

🔐 Security & Ethical Use
DO NOT use this on systems you do not own or have permission to monitor.
Use this tool only for ethical hacking, personal security, or educational purposes.

🛠 Troubleshooting
❓ Email not sending?➡️ Check if your email credentials are correct. If using Gmail, enable less secure apps or use App Passwords.
❓ Log file not encrypting?➡️ Ensure filekey.key exists and is properly generated.

📜 License
This project is licensed under the MIT License. Feel free to modify and use it responsibly.

🤝 Contributing
Want to improve this project? Fork it and submit a pull request!

📬 Contact
For questions or issues, open a GitHub issue or contact karandeep.multani18@gmail.com
