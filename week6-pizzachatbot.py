print("Hello, my name is your virtual assistant. I will help you order a pizza!")
print("I'm going to ask you a few questions. After typing an answer, press enter.")

keepGoing = "y"

while keepGoing.lower() == "y":

    userName = input("Enter your name: ").lower()
    while len(userName) == 0:
        print("Name cannot be blank! Please enter your name.")
        userName = input("Enter your name: ").lower()

    if userName == "tyquan wilson":
        print(f"\nMy creator, {userName}. Pleasure to serve you!")
    else:
        print(f"\nHello, {userName}. Nice to meet you!")

    # ==== PIZZA INFO VALIDATION ====

    # Size
    size = input("What size pizza? (small, medium, large): ").lower()
    while size not in ["small", "medium", "large"]:
        size = input("Invalid size! Enter small, medium, or large: ").lower()

    # Flavor
    flavor = input("What flavor? (cheese, pepperoni, veggie, etc.): ").lower()
    while len(flavor) == 0:
        print("Flavor cannot be blank! Enter a flavor:")
        flavor = input("What flavor? ").lower()

    # Crust
    crustType = input("What crust type? (thin, regular, stuffed): ").lower()
    while crustType not in ["thin", "regular", "stuffed"]:
        crustType = input("Invalid crust! Enter thin, regular, or stuffed: ").lower()

    # Quantity must be numeric
    quantity = input("How many of these do you want to order? Enter a numeric value: ")
    while not quantity.isdigit():
        print("Value not recognized. Please enter a numeric value.")
        quantity = input("How many of these do you want to order? ")
    quantity = int(quantity)

    # Delivery Validation
    orderType = input("Delivery or carryout?: ").lower()
    while orderType not in ["delivery", "carryout", "carry-out", "carry out"]:
        orderType = input("Invalid entry! Type 'delivery' or 'carryout': ").lower()

    # Delivery fee
    deliveryFee = 0
    if orderType == "delivery":
        deliveryFee = 5

    # ==== PRICE LOGIC ====
    if size == "small":
        pizzaCost = 10.99
    elif size == "medium":
        pizzaCost = 12.99
    else:
        pizzaCost = 17.99

    subtotal = (pizzaCost * quantity) + deliveryFee

    # Coupon Logic
    coupon = 0
    if subtotal > 50:
        coupon = 10

    # ==== OUTPUT ====
    print("\n---- ORDER SUMMARY ----")
    print(f"Customer: {userName}")
    print(f"Pizza size: {size}")
    print(f"Flavor: {flavor}")
    print(f"Crust: {crustType}")
    print(f"Quantity: {quantity}")
    print(f"Order Type: {orderType}")
    print(f"Delivery Fee: ${deliveryFee:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")

    if coupon > 0:
        print(f"Order over $50 will receive a free $10 OFF coupon!")

    # ==== COUNTDOWN TIMER ====
    print("Order has been received. ETA 3 mins!")

    for min in range(3, 0, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end="\r")
            import time
            time.sleep(1)

    print("Order is ready!")

    # Ask if they want another
    keepGoing = input("Do you want to place another order? Enter y or n: ").lower()
    while keepGoing not in ["y", "n"]:
        keepGoing = input("Invalid value. Enter y or n: ").lower()

print("Thank you for using the pizza chatbot!")