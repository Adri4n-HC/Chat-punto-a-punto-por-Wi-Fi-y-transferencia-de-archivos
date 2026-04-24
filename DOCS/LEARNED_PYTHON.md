# Resumen de Conceptos y Funciones Aprendidas en Python

Durante el desarrollo de este proyecto de chat punto a punto y transferencia de archivos, se aplicaron y consolidaron diversos conceptos fundamentales de Python, orientados a redes, concurrencia y buenas prácticas.

## 1. Sockets y Funciones Clave
La librería `socket` es la base de la comunicación en red. Comprendimos el flujo de vida de una conexión TCP:
* `socket()`: Crea el objeto socket, definiendo la familia de direcciones (ej. `AF_INET` para IPv4) y el tipo de socket (`SOCK_STREAM` para TCP).
* `bind()`: Asocia el socket del servidor a una dirección IP y un puerto específicos.
* `listen()`: Pone al servidor en modo de escucha, indicando cuántas conexiones en cola puede aceptar.
* `accept()`: Bloquea la ejecución hasta que un cliente se conecta, devolviendo un nuevo objeto de conexión y la tupla de la dirección del cliente.
* `connect()`: Usado por el cliente para intentar establecer una conexión con la IP y puerto del servidor.
* `sendall()`: A diferencia de `send()`, garantiza que todos los bytes del mensaje se transmitan a través de la red antes de continuar.
* `recv()`: Lee los datos recibidos en el buffer (especificando la cantidad de bytes, ej. 1024).

## 2. Manejo de Archivos
Para la mejora de transferencia de archivos, se aprendió a manejar datos crudos en lugar de solo texto:
* **`open()`**: Uso del modo `'rb'` (read binary) para leer archivos y `'wb'` (write binary) para guardarlos.
* **Lectura por bloques (chunks)**: En lugar de cargar un archivo de 10 MB completo en la memoria RAM, se lee y se envía en fragmentos (ej. `file.read(4096)`), lo cual hace el programa eficiente y escalable.

## 3. Hashing
* **`hashlib`**: Se implementó `hashlib.sha256()` para garantizar la integridad de los archivos transferidos. Al leer el archivo en el cliente, se actualiza el hash por cada bloque. El servidor repite este proceso al recibir el archivo y compara ambos checksums para confirmar que no hubo corrupción de datos durante el envío.

## 4. Logging
* **`logging`**: Se reemplazó el uso excesivo de `print()` por el módulo `logging`. Esto permite registrar eventos (conexiones, errores, transferencias) con marcas de tiempo y niveles de severidad (`INFO`, `WARNING`, `ERROR`), facilitando la depuración y guardando el historial en archivos `.log`.

## 5. Argparse
* **`argparse`**: Se comprendió cómo parametrizar la ejecución de los scripts desde la terminal de comandos. Mediante esta librería, es posible iniciar el cliente o servidor especificando argumentos como `--host 192.168.1.5`, `--port 5050` o `--file archivo.txt` sin tener que modificar el código fuente.

## 6. Concurrencia Básica
Dado que `recv()` y `accept()` son funciones bloqueantes, se analizó cómo mantener el programa responsivo:
* **`threading`**: (Método utilizado en el chat base). Permite ejecutar funciones en hilos paralelos (ej. un hilo para escuchar mensajes y el programa principal para enviarlos). Ideal para operaciones I/O limitadas.
* **`select`**: Permite monitorear múltiples sockets en un solo hilo para ver cuáles están listos para lectura o escritura.
* **`asyncio`**: Proporciona concurrencia de un solo hilo mediante bucles de eventos (event loops) y corrutinas (`async/await`). Se recomienda para servidores que deben manejar miles de conexiones simultáneas.

## 7. Utilidades del Sistema
* **`pathlib`**: Usado para un manejo moderno y multiplataforma de las rutas de archivos (ej. asegurar que el archivo se guarde en `results/received/`).
* **`os`**: Útil para verificar si un archivo existe antes de enviarlo o para obtener su tamaño en bytes (`os.path.getsize()`).
* **`subprocess`**: Permite ejecutar comandos del sistema operativo desde Python, como invocar los scripts de `.bat` o `.sh` para crear el hotspot automáticamente.

## 8. Buenas Prácticas Aplicadas
* **Mensajes de commit claros:** Adopción de convenciones semánticas (`feat:`, `fix:`, `docs:`) para mantener un historial trazable y profesional.
* **Protocolo de envío de metadatos:** Aprendimos que antes de enviar un flujo de bytes crudos, es obligatorio enviar un "encabezado" que indique al receptor qué está a punto de recibir (ej. `FILENAME|SIZE|SHA256\n`), permitiendo al servidor preparar el archivo destino.
* **Manejo de errores:** Uso de bloques `try-except` para atrapar desconexiones abruptas (`ConnectionResetError`) o interrupciones de teclado (`KeyboardInterrupt`), cerrando siempre los sockets limpiamente usando `.close()`.
