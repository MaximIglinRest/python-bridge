from abc import ABC, abstractmethod

from src.notifications import NotificationService
from src.payments import PaymentService


class Application(ABC):
    def __init__(
        self, payment_service: PaymentService, notification_service: NotificationService
    ):
        self.payment_service = payment_service
        self.notification_service = notification_service

    @abstractmethod
    def complete_transaction(self, amount: float, notification_message: str):
        pass


class ECommerceApplication(Application):
    def complete_transaction(self, amount: float, notification_message: str):
        self.payment_service.process_payment(amount)
        self.notification_service.send_notification(notification_message)


class SubscriptionApplication(Application):
    def complete_transaction(self, amount: float, notification_message: str):
        self.payment_service.process_payment(amount)
        self.notification_service.send_notification(notification_message)
