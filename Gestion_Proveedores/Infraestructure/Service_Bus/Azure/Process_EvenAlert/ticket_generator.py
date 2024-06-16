import uuid

def generate_ticket(event_data):
    """Genera un TicketId para el evento de alarma."""
    ticket_id = str(uuid.uuid4())
    return f"Generated TicketId: {ticket_id} for event: {event_data}"
