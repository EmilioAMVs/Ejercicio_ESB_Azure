from azure.servicebus import ServiceBusClient

def get_servicebus_client(connection_str):
    """Crea y retorna un cliente de Service Bus."""
    return ServiceBusClient.from_connection_string(conn_str=connection_str, logging_enable=True)
