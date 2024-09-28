from abc import ABC, abstractmethod


class PaymentService(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class StripeService(PaymentService):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through Stripe.")


class PayPalService(PaymentService):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")
