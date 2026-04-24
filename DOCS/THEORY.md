# Teoría de Redes y Sockets

Este documento detalla los conceptos fundamentales de comunicación en red necesarios para el desarrollo de aplicaciones cliente-servidor.

## 1. ¿Qué es un socket?
Un **socket** es un punto final (endpoint) en un enlace de comunicación bidireccional entre dos programas que se ejecutan en una red. Se compone de una dirección IP y un número de puerto.

* **Definición breve:** Es la interfaz que permite a un proceso enviar o recibir datos hacia/desde otro proceso, ya sea en la misma máquina o a través de Internet.
* **Ejemplo de uso:** En una arquitectura de chat, el cliente abre un socket para conectarse a la dirección IP del servidor en el puerto 5000. El servidor, a su vez, mantiene un socket abierto escuchando peticiones en ese mismo puerto para establecer el canal de mensajes.

## 2. TCP vs UDP
Los dos protocolos de transporte más utilizados tienen características opuestas según la necesidad del sistema.

| Característica | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Conexión** | Orientado a conexión (requiere handshake). | Sin conexión (envía y olvida). |
| **Fiabilidad** | Alta: retransmite paquetes perdidos. | Baja: puede haber pérdida de datos. |
| **Orden** | Garantiza que los datos lleguen en orden. | No garantiza el orden de llegada. |
| **Velocidad** | Más lento por la sobrecarga de control. | Muy rápido y ligero. |
| **Uso ideal** | Web (HTTP), Email (SMTP), Transferencia de archivos (FTP). | Streaming de video, Juegos online, VoIP. |



## 3. Puertos y Direcciones IP
Para que la comunicación ocurra, se necesitan dos identificadores:
* **Dirección IP:** Identifica de forma única a un host en la red.
* **Puerto:** Identifica un proceso o servicio específico dentro de ese host.

### Clasificación de Puertos:
* **Puertos bien conocidos (0 - 1023):** Reservados para servicios del sistema y protocolos estándar (ej: HTTP 80, HTTPS 443, SSH 22).
* **Puertos registrados (1024 - 49151):** Usados por aplicaciones de usuario o procesos específicos.
* **Puertos dinámicos/privados (49152 - 65535):** Asignados temporalmente por el SO al cliente cuando inicia una conexión.

## 4. NAT y problemas de conectividad
**NAT (Network Address Translation)** es el mecanismo que permite que varios dispositivos en una red privada (como tu casa) salgan a Internet usando una única dirección IP pública.

* **Problema común:** Como los dispositivos internos tienen IPs privadas (no visibles desde afuera), un servidor externo no puede iniciar una conexión hacia un cliente detrás de un NAT a menos que se configure **Port Forwarding** o se usen técnicas de "Hole Punching". Esto es crítico al desarrollar apps P2P.

## 5. Firewalls y permisos de puerto
Un firewall actúa como un filtro de seguridad que bloquea tráfico no deseado.
* **Desarrollo:** Al programar sockets, es común que la conexión falle aunque el código sea correcto. Esto sucede porque el firewall del sistema operativo (o del router) bloquea el puerto elegido.
* **Solución:** Se deben añadir "Reglas de entrada" para permitir el tráfico en el puerto específico que la aplicación va a utilizar.

## 6. Wi-Fi Direct vs Hotspot vs Misma Red


* **Misma Red (Infraestructura):** Ambos dispositivos se conectan a un router común. La latencia depende de la calidad del router.
* **Hotspot:** Un dispositivo crea una red y el otro se une. Es útil cuando no hay internet, pero el "host" consume más recursos.
* **Wi-Fi Direct:** Conexión directa de hardware a hardware sin intermediarios. Ofrece mayor velocidad de transferencia que Bluetooth y no requiere un router, pero la implementación de sockets requiere manejar la negociación de roles (Group Owner).

## 7. Seguridad básica: TLS/SSL
La comunicación por sockets estándar viaja en texto plano. **TLS (Transport Layer Security)**, sucesor de SSL, cifra esta comunicación.

### Recomendaciones para pruebas:
1.  **Cifrado:** Utilizar librerías que implementen `SSLSocket` en lugar de sockets estándar para proteger datos sensibles.
2.  **Certificados:** Durante el desarrollo, se pueden usar certificados auto-firmados, pero en producción se deben usar certificados emitidos por una autoridad (CA).
3.  **Validación:** Siempre validar los datos de entrada en el servidor para evitar ataques de inyección, incluso si el canal está cifrado.
