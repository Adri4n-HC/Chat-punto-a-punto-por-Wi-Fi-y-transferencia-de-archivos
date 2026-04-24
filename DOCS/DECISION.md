# Decisiones de Diseño y Red

## 1. Método Elegido
Para la implementación de este chat punto a punto, se seleccionó el método de **Hotspot (Punto de acceso móvil) alojado en Windows**. Una de las laptops actúa como host creando la red, y la otra se conecta a ella como cliente.

## 2. Justificación de la Elección
Se evaluaron opciones como conectarse a una misma red local (Wi-Fi existente) o usar Wi-Fi Direct, pero el Hotspot resultó ser la opción más viable por las siguientes razones:

* **Ventajas:**
  * **Evasión de AP Isolation:** Las redes públicas o institucionales (como el Wi-Fi del campus) suelen tener activado el *AP Isolation* por seguridad, lo cual impide que dos dispositivos conectados a la misma red se comuniquen entre sí (haciendo imposible el P2P). Al crear nuestro propio Hotspot, tenemos control total sobre el tráfico local.
  * **Independencia de hardware externo:** No dependemos de un router físico para establecer la LAN.
  * **Asignación de IP predecible:** El equipo host suele tomar una dirección IP estática dentro de su propia subred (frecuentemente `192.168.137.1`), lo que facilita la configuración del cliente.

* **Limitaciones:**
  * Depende de que la tarjeta de red de la laptop anfitriona soporte la creación de redes hospedadas.
  * El alcance físico es limitado a la potencia de la antena de la laptop anfitriona (usualmente unos pocos metros).

## 3. Comandos Usados (Windows)
Para automatizar y gestionar la creación de la red ad-hoc/hotspot desde la terminal de Windows (CMD como administrador), se utilizaron los siguientes comandos a través de la utilidad `netsh`:

* **Crear y configurar el hotspot:**
  `netsh wlan set hostednetwork mode=allow ssid="Chat_P2P_Equipo" key="redes12345"`
* **Iniciar el hotspot:**
  `netsh wlan start hostednetwork`
* **Verificar la IP asignada al servidor:**
  `ipconfig` (Buscando el adaptador LAN inalámbrico Conexión de área local*).
* **Detener el hotspot (al finalizar):**
  `netsh wlan stop hostednetwork`

## 4. Problemas Encontrados y Soluciones
Durante la fase de pruebas, nos enfrentamos a los siguientes obstáculos:

1. **Problema:** El cliente devolvía el error `ConnectionRefusedError: [WinError 10061]` a pesar de estar conectados al mismo Hotspot.
   * **Solución:** El Firewall de Windows Defender del equipo servidor estaba bloqueando las conexiones entrantes. Se resolvió creando una regla de entrada en el Firewall para permitir el tráfico TCP en el puerto `5050`, o alternativamente, configurando la red del Hotspot como "Privada" en lugar de "Pública".
2. **Problema:** Confusión con la dirección IP al conectar el cliente.
   * **Solución:** Al ejecutar `ipconfig`, el sistema mostraba múltiples adaptadores (VirtualBox, Wi-Fi principal, etc.). Se documentó que el cliente debe usar estrictamente la dirección IPv4 correspondiente al adaptador de la red hospedada creada por `netsh`, ignorando la IP del Wi-Fi que da salida a internet.
