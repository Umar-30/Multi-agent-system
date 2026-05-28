class MessageBus:
    def __init__(self):
        self.messages = []

    def send(self, sender, receiver, content):
        self.messages.append({
            "sender": sender,
            "receiver": receiver,
            "content": content
        })

    def get_messages(self):
        return self.messages