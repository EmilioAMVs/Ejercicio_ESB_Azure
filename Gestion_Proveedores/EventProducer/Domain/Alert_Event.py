class EventAlert:
    def __init__(self, server, message):
        self.server = server
        self.message = message

    def __str__(self):
        return f"Alerta del servidor {self.server}: {self.message}"