import stripe
from config.settings import STRIPE_SK

stripe.api_key = STRIPE_SK


def create_session(currency, name, price, discount_id=None):
    if not discount_id:
        discount_id = None
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
        discounts=[{'coupon': discount_id}],
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return { 'id': session.id }