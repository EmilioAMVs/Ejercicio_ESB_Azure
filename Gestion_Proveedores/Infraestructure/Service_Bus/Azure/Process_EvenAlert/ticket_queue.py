from servicebus_client import get_servicebus_client
from queue_reciever import receive_message_from_queue
from ticket_generator import generate_ticket
from queue_sender import send_message_to_queue

def main():
    CONNECTION_STR = ''
    INCIDENTS_QUEUE_NAME = 'incidents'
    TICKETS_QUEUE_NAME = 'ticket'

    # Obtener el cliente de Service Bus
    servicebus_client = get_servicebus_client(CONNECTION_STR)

    # Recibir el evento de alarma de la cola 'incidents'
    event_data = receive_message_from_queue(servicebus_client, INCIDENTS_QUEUE_NAME)
    if event_data:
        # Generar un TicketId para el evento
        ticket_data = generate_ticket(event_data)

        # Enviar el TicketId a la cola 'tickets'
        send_message_to_queue(servicebus_client, TICKETS_QUEUE_NAME, ticket_data)

if __name__ == "__main__":
    main()
