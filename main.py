# Menu prices
from pyscript import display, document


# Menu prices
PRICES = {
    "americano": 155.00,
    "latte": 165.50,
    "coldbrew": 165.00,
    "affogato": 155.00,
    "caramel": 185.00,
    "cookie": 210.00,
    "matcha": 185.50

}

TAX_RATE = 0.10

def create_order(e):
    subtotal = 0
    # Sum selected items
    for item_id, price in PRICES.items():
        if document.getElementById(item_id).checked:
            subtotal += price

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Display receipt
    display(f"Subtotal: ₱{subtotal:.2f}", target="receipt")
    display(f"Tax: ₱{tax:.2f}", target="receipt")
    display(f"Total: ₱{total:.2f}", target="receipt")