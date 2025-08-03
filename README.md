🕵️‍♂️ Remote Keylogger Project (Python)

A Python-based remote keylogger tool designed for educational and ethical use only. It captures keyboard input and sends it either via email or to a remote TCP socket server for analysis.

---------------------------------------------------

🚀 Features

- 🎯 Captures all keystrokes (including special keys)
- 📤 Sends logs:
  - Via SMTP email
  - Over TCP socket to a remote listener
- 📅 Automatic email reporting every 5 minutes (configurable)
- 🧵 Threaded operation for smooth logging and reporting
- 💻 Cross-platform support (Windows/Linux)

---------------------------------------------------

⚙️ Installation

✅ Requirements
- Python 3.6 or above
- Libraries:
  - pynput
  - schedule

📦 Install Dependencies
pip install pynput schedule

---------------------------------------------------

🧠 Usage

📧 Email Keylogger

1. Open keylogger_email.py
2. Configure:
   EMAIL_ADDRESS = "your_email@gmail.com"
   EMAIL_PASSWORD = "your_app_password"
   TO_ADDRESS = "recipient@example.com"

   ⚠️ Use an App Password if 2FA is enabled on Gmail.

3. Run:
   python keylogger_email.py

---------------------------------------------------

🌐 Socket Keylogger

On Attacker (Listener) Machine:
python keylogger_server.py

On Victim Machine:
1. Open keylogger_client.py
2. Set the IP:
   SERVER_IP = "attacker-ip-address"
   PORT = 4444

3. Run:
   python keylogger_client.py

---------------------------------------------------

🔐 Ethical Disclaimer

This tool is intended strictly for educational, ethical hacking, and penetration testing purposes with proper authorization. Unauthorized use of this tool is illegal and unethical.

---------------------------------------------------

🔮 Future Improvements

- AES encrypted keylogs
- GUI dashboard to monitor logs
- Log persistence & auto-start on boot
- Log upload to cloud storage

---------------------------------------------------

📁 Project Structure

remote_keylogger_project/
├── keylogger_email.py       # Sends keylogs via email
├── keylogger_client.py      # Sends keylogs over socket
├── keylogger_server.py      # Receives and displays keylogs
└── README.txt               # Project documentation

---------------------------------------------------

🧑‍💻 Author

Sahil Koli  
Penetration Tester | Ethical Hacker  
GitHub: https://github.com/jokersk551

---------------------------------------------------

📬 Contact

Email: sahilkoliethical@gmail.com  
Instagram: 
