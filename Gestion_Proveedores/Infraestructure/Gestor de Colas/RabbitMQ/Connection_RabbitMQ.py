import pika

def rabbitmqConnection():
 # Conexión al servidor RabbitMQ
    return pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    
def rabbitmqChannel(connection):    
    return connection.channel()