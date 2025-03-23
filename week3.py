def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        new_price = (price * (100 - discount_percent)) / 100
    else:
        new_price = price
    return  new_price
price = int(input("what's the price of the item: "))
discount_percent = int(input("what's the item'e \%\ discount: "))

disc = calculate_discount(price, discount_percent)
print(disc)