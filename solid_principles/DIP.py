from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailSender(MessageSender):
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender

    def send_notification(self, recipient, message):
        self.message_sender.send(recipient, message)


# Using the NotificationService to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification(
    "riyaz@fusemachines.com", "Hello, this is a notification!")