# consumer.py

import os.path
import base64
import pickle
import os
import json
import google.auth
import google_auth_oauthlib.flow
import google.auth.transport.requests
import googleapiclient.discovery
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
import pika
from Connection_RabbitMQ import rabbitmqConnection,rabbitmqChannel
from EventProducer.Domain.Alert_Event import EventAlert

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def send_email(creds, subject, body, destinatario):
    try:
        service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
        message = MIMEText(body)
        message['to'] = destinatario
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message = {'raw': raw}
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        print(f" [x] Correo enviado a {destinatario}, ID del mensaje: {sent_message['id']}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def callback(ch, method, properties, body):
    print(f"[x] Recibido: {body.decode()}")
    data = json.loads(body.decode())
    alert = EventAlert(data['server', data['message']])
    send_email(authenticate_gmail(), f'Alerta: {alert.server}', str(alert), 'destinatario@example.com')

def consume_message():
    connection = rabbitmqConnection()
    channel = rabbitmqChannel(connection)

    channel.queue_declare(queue='test_queue')

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Esperando mensajes. Para salir presione CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_message()
