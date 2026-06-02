def calculate_total(price_per_meal, number_of_meals):
    return price_per_meal * number_of_meals


def calculate_delivery_fee(order_total):
    if order_total >= 500:
        return 0

    return 40


def format_money(amount):
    return f"Rs {amount}"
