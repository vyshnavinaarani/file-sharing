import socket
import os

def send_file(conn, filename):
    # Specify the directory where files are stored
    file_path = os.path.join("shared_files", filename)

    # Check if the file exists
    if os.path.exists(file_path):
        conn.send(f"EXISTS {os.path.getsize(file_path)}".encode())
        response = conn.recv(1024).decode()

        # If the client is ready to receive the file
        if response == "READY":
            with open(file_path, "rb") as file:
                data = file.read(1024)
                while data:
                    conn.send(data)
                    data = file.read(1024)
            print(f"File '{filename}' sent successfully.")
    else:
        conn.send("ERR File not found".encode())

def main():
    host = "0.0.0.0"  # Listen on all available network interfaces
    port = 8080       # Port number to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

        # Receive the file request from client
        filename = conn.recv(1024).decode()
        print(f"File requested: {filename}")
        send_file(conn, filename)

        conn.close()

if __name__ == "__main__":
    main()
