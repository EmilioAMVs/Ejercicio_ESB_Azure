from servicebus_client import get_servicebus_client
from queue_sender import send_message_to_queue
from message_processor import process_alarm_event

def main():
    CONNECTION_STR = ''
    QUEUE_NAME = 'incidents'
    raw_event_data = "AlarmEvent: Fallo con un equipo, se necesita de su servicio para dar mantenimiento"

    # Procesar el evento de alarma
    processed_event_data = process_alarm_event(raw_event_data)

    # Obtener el cliente de Service Bus
    servicebus_client = get_servicebus_client(CONNECTION_STR)

    # Enviar el evento procesado a la cola
    send_message_to_queue(servicebus_client, QUEUE_NAME, processed_event_data)

if __name__ == "__main__":
    main()
