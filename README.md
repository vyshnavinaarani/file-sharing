
# File Sharing Project using Python (Socket Programming)

This is a simple client-server based File Sharing System implemented using Python's socket programming. The server hosts files, and the client can request and download files from the server over a network.

---

## 🚀 How to Run the Project

### ✅ To Run the Server:
1. Open a terminal.
2. Navigate to the `server` directory.
3. Run the server script:
   ```bash
   python server.py
````

### ✅ To Run the Client:

1. Open another terminal.
2. Navigate to the `client` directory.
3. Run the client script:

   ```bash
   python client.py
   ```
4. When prompted:

   * Enter the **server's IP address** (use `127.0.0.1` for localhost testing).
   * Enter the **filename** you want to download (e.g., `file1.txt`).

---

## 📁 Directory Structure

```
file_sharing_project/
├── server/
│   ├── server.py
│   └── shared_files/
│       ├── file1.txt
│       ├── file2.pdf
│       ├── image.jpg
│       └── document.docx
└── client/
    └── client.py
```

* All files available for sharing must be placed inside the `shared_files/` folder in the server directory before running the server.

---

## 🧠 Features

* Client-Server file transfer using TCP sockets
* Supports different file types (text, PDF, images, etc.)
* Chunk-based file transfer for efficiency
* Error message if the file is not found

---

## 📌 Notes

* Ensure both `server.py` and `client.py` are run using Python 3.
* For LAN testing, replace `127.0.0.1` with the actual IP address of the server machine.
* Received files on the client side will be saved as `received_<filename>`.

---

## 📚 Technologies Used

* Python 3
* Socket Programming (TCP)
* File Handling

---

