import stripe
from config.settings import STRIPE_SK

stripe.api_key = STRIPE_SK


def create_session(currency, name, price):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': name,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return { 'id': session.id }