def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount=price*(discount_percent/100)
        return price-discount
    else:
        return price
    
price=float(input("Enter the price of the item: "))
discount_percent=float(input("Enter the discount percentage: "))

final_price=calculate_discount(price, discount_percent)
print(f"The final price after discount is: {final_price}")