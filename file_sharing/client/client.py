import socket

def receive_file(filename, conn):
    # Save the file as received_<filename> in the client directory
    with open(f"received_{filename}", "wb") as file:
        data = conn.recv(1024)
        while data:
            file.write(data)
            data = conn.recv(1024)
    print(f"File '{filename}' received successfully.")

def main():
    host = input("Enter server IP: ")  # IP of the server
    port = 8080                        # Port number of the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = input("Enter the filename to request: ")
    client_socket.send(filename.encode())

    response = client_socket.recv(1024).decode()
    if response.startswith("EXISTS"):
        filesize = int(response.split()[1])
        print(f"File exists. Size: {filesize} bytes.")
        answer = input("Do you want to download it? (yes/no): ").strip().lower()

        if answer == "yes":
            client_socket.send("READY".encode())
            receive_file(filename, client_socket)
        else:
            print("Download cancelled.")
    else:
        print("File not found on the server.")

    client_socket.close()

if __name__ == "__main__":
    main()
