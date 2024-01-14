number_of_orders = int(input())
price_per_capsule = float(input())
days = int(input())
capsules_needed = int(input())
price = 0
total_price = 0
check = True
while number_of_orders != 0:
    check = True
    number_of_orders -= 1
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        check = False
    elif days < 1 and days > 31:
        check = False
    elif capsules_needed < 1 or capsules_needed > 2000:
        check = False


    if check == True:
        price = (price_per_capsule * capsules_needed * days)
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
    if number_of_orders > 0:
        price_per_capsule = float(input())
        days = int(input())
        capsules_needed = int(input())




print(f"Total: ${total_price:.2f}")