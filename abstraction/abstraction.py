# The goal of this program is to process a customer's order at a coffee shop


def main():
    ''' our main function is much more clear '''
    prices = get_prices()

    orders = get_orders(prices)

    totals = calculate_totals(prices, orders)

    subtotal = add_totals(totals)

    total = apply_discount(subtotal)

    print_receipt(orders, totals, subtotal, total)


    

def get_prices():
    prices = {
        "coffees": 3.50,
        "teas": 2.75,
        "pastries": 4.0
    }
    return prices

def get_orders(prices):
    orders = {}
    for item in prices.keys():
        amount = int(input(f"How many {item} would you like? "))
        orders[item] = amount
    return orders

def calculate_totals(prices, orders):
    totals = {}
    for item, quantity in orders.items():
        totals[item] = prices[item] * quantity
    
    return totals

def add_totals(totals):
    added_total = 0
    for total in totals.values():
        added_total += total
    return added_total

def apply_discount(total):
    discount_rate = 0.1
    # Apply discount if the subtotal is over $20
    if total > 20:
        discount = total * discount_rate
        print(f"Discount applied: ${discount:.2f}")
        return total - discount
    else:
        total = total

def print_receipt(orders, totals, subtotal, total):
    print("Receipt:")
    for item, quantity in orders.items():
        print(f"{quantity} {item}: ${totals[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")

    


if __name__ == "__main__":
    main()
