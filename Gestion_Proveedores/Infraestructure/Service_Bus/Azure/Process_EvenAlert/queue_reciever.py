def receive_message_from_queue(servicebus_client, queue_name):
    """Recibe un mensaje de una cola específica del Service Bus."""
    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=queue_name)
        with receiver:
            messages = receiver.receive_messages(max_message_count=1, max_wait_time=5)
            for message in messages:
                message_body = b''.join([bytes(b) for b in message.body])
                print(f"Mensaje recibido: {message_body.decode('utf-8')}")
                receiver.complete_message(message)
                return message_body.decode('utf-8')
    return None
