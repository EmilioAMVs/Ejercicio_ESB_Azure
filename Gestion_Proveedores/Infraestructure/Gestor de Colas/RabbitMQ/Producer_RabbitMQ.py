
import pika
from Connection_RabbitMQ import rabbitmqConnection, rabbitmqChannel
from EventProducer.Domain.Alert_Event import EventAlert
import json

def send_message(event_alert):
    connection = rabbitmqConnection()
    channel = rabbitmqChannel(connection)

    channel.queue_declare(queue='test_queue')

    message = json.dumps({
        'server': event_alert.server,
        'message': event_alert.message
    })

    channel.basic_publish(exchange='',
                          routing_key='test_queue',
                          body=message)

    print(f" [x] Enviado '{message}'")
    connection.close()

if __name__ == "__main__":
    alert = EventAlert('Servidor1', 'Este es un mensaje de prueba.')
    send_message(alert)
