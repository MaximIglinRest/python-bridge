from src.application import ECommerceApplication, SubscriptionApplication
from src.notifications import TwilioService, EmailService
from src.payments import StripeService, PayPalService

if __name__ == "__main__":
    # Использование Stripe и Twilio
    stripe_service = StripeService()
    twilio_service = TwilioService()

    ecommerce_app = ECommerceApplication(stripe_service, twilio_service)
    ecommerce_app.complete_transaction(100.0, "Thank you for your purchase!")

    # Использование PayPal и Email
    paypal_service = PayPalService()
    email_service = EmailService()

    subscription_app = SubscriptionApplication(paypal_service, email_service)
    subscription_app.complete_transaction(50.0, "Your subscription has been activated!")
