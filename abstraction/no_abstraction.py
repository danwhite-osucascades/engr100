# The goal of this program is to process a customer's order at a coffee shop


def main():
    ''' Everything is inside of our main function '''

    # Customer chooses items
    coffee_price = 3.50
    tea_price = 2.75
    pastry_price = 4.00
    discount_rate = 0.1  # 10% discount

    # Items ordered
    coffee_qty = int(input("How many coffees would you like? "))
    tea_qty = int(input("How many teas would you like? "))
    pastry_qty = int(input("How many pastries would you like? "))

    # Calculating total
    coffee_total = coffee_qty * coffee_price
    tea_total = tea_qty * tea_price
    pastry_total = pastry_qty * pastry_price
    subtotal = coffee_total + tea_total + pastry_total

    # Apply discount if the subtotal is over $20
    if subtotal > 20:
        discount = subtotal * discount_rate
        total = subtotal - discount
        print(f"Discount applied: ${discount:.2f}")
    else:
        total = subtotal

    # Print receipt
    print("Receipt:")
    print(f"{coffee_qty} coffee(s): ${coffee_total:.2f}")
    print(f"{tea_qty} tea(s): ${tea_total:.2f}")
    print(f"{pastry_qty} pastry(s): ${pastry_total:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")


    





if __name__ == "__main__":
    main()
