from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Cadena de conexión del namespace del Service Bus
CONNECTION_STR = "llenar con el propio"

# Nombre de la cola
QUEUE_NAME = 'notificacionesproveedor'

# Crear un cliente de Service Bus
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

# Enviar un mensaje a la cola
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        # Crear un mensaje
        message = ServiceBusMessage("Hola, este es un mensaje enviado desde Python")
        # Enviar el mensaje
        sender.send_messages(message)
        print("Mensaje enviado")

