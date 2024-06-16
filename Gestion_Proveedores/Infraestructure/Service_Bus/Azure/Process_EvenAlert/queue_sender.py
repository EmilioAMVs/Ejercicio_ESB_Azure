from azure.servicebus import ServiceBusMessage

def send_message_to_queue(servicebus_client, queue_name, message_text):
    """Envía un mensaje a una cola específica del Service Bus."""
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=queue_name)
        with sender:
            message = ServiceBusMessage(message_text)
            sender.send_messages(message)
            print(f"Mensaje enviado a la cola {queue_name}")
