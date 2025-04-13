import stripe
from flask import current_app

def create_payment_intent(amount, currency='usd'):
    stripe.api_key = current_app.config['STRIPE_API_KEY']
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )