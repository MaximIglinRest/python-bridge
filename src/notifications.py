from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class TwilioService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending notification via Twilio: {message}")


class EmailService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending notification via Email: {message}")
