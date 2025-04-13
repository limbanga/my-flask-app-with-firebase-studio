import stripe
from app import app

stripe.api_key = app.config['STRIPE_API_KEY']

def create_checkout_session(amount, movie_title):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': f"Ticket: {movie_title}"},
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
    )