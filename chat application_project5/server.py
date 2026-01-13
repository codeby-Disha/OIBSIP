import socket

def start_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
 
    host = '127.0.0.1'  # Localhost
    port = 12345        # Any non-privileged port
    server_socket.bind((host, port))
    
    
    server_socket.listen(1)
    print(f"Server started. Waiting for a connection on {host}:{port}...")
    
   
    conn, addr = server_socket.accept()
    print(f"Connected by: {addr}")
    
    while True:
        # Receive data (up to 1024 bytes)
        data = conn.recv(1024).decode('utf-8')
        if not data or data.lower() == 'bye':
            print("Client disconnected.")
            break
        print(f"Client: {data}")
        
        # Send a response
        response = input("Server (You): ")
        conn.send(response.encode('utf-8'))
        if response.lower() == 'bye':
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":

    start_server()
