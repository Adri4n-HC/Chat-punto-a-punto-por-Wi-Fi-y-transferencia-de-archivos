import socket
import threading
import sys

# Configuración: 0.0.0.0 permite conexiones desde cualquier IP en tu red
HOST = '0.0.0.0' 
PORT = 5050

def receive_messages(conn):
    """Función que se ejecuta en un hilo separado para escuchar mensajes continuamente."""
    while True:
        try:
            # Recibe hasta 1024 bytes y los decodifica a texto
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"\n[Cliente]: {msg}")
        except:
            break
    print("\n[!] Conexión cerrada.")
    conn.close()
    sys.exit()

def start_server():
    # Crear el socket TCP (IPv4, flujo de datos)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1) # Escucha a 1 cliente a la vez
    print(f"[+] Servidor escuchando en el puerto {PORT}...")

    # Espera a que un cliente se conecte
    conn, addr = server.accept()
    print(f"[+] Conexión establecida con la IP: {addr[0]}")

    # Inicia un hilo paralelo solo para recibir mensajes
    thread = threading.Thread(target=receive_messages, args=(conn,))
    thread.daemon = True # El hilo muere si el programa principal se cierra
    thread.start()

    # Bucle principal para ENVIAR mensajes
    while True:
        try:
            msg = input()
            conn.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            # Si presionas Ctrl+C, cierra todo limpiamente
            print("\n[!] Cerrando servidor.")
            conn.close()
            break

if __name__ == "__main__":
    start_server()
