import socket
import threading
import sys

PORT = 5050

def receive_messages(client):
    """Escucha mensajes del servidor en segundo plano."""
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"\n[Servidor]: {msg}")
        except:
            break
    print("\n[!] Conexión cerrada por el servidor.")
    client.close()
    sys.exit()

def start_client():
    # Pide la IP. Si pruebas en la misma compu, usa 127.0.0.1
    host = input("Ingresa la IP del servidor (ej. 127.0.0.1 para local): ")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, PORT))
        print(f"[+] Conectado al servidor {host}:{PORT}")
    except Exception as e:
        print(f"[!] Error al conectar: {e}")
        return

    # Inicia el hilo para recibir
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    # Bucle para enviar
    while True:
        try:
            msg = input()
            client.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            print("\n[!] Desconectando.")
            client.close()
            break

if __name__ == "__main__":
    start_client()
