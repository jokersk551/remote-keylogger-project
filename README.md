# Python Keylogger with Remote TCP Socket

## 🔧 Installation Steps

1. **Clone or Extract the Project**
   ```
   unzip python_keylogger_socket.zip
   cd python_keylogger_socket
   ```

2. **Install Required Library**
   ```
   pip install pynput
   ```

3. **Run the Server (Receiver)**
   On the machine that will receive keystrokes:
   ```
   python receiver.py
   ```

4. **Run the Keylogger (Client)**
   On the machine where keystrokes are captured:
   - Open `keylogger_remote_socket.py`
   - Set `SERVER_IP` to your server's IP
   - Then run:
   ```
   python keylogger_remote_socket.py
   ```

## ⚠️ Legal and Ethical Notice

This tool is for **educational purposes only**. Do not deploy this script on any system without full consent and authorization.

Using this on devices without permission may be illegal and unethical.
