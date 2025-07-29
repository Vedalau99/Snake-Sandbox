people = int(input("How many people  ")) 

def greet(name):   
    print(f"Hello, {name}!")

grand_total = 0 
receipt = []

menu = {"orange": 50, "apple": 60, "mango": 70}

while people != 0:
    people -= 1
    customers = input("Enter your name  ")
    greet(customers)

    wants_menu = input("Would you like to see the menu? (yes/no): ").lower()
    if wants_menu == "yes":
        print("Here's the menu:")
        for item, price in menu.items():
            print(f"{item.title()} - ₹{price}")

    customer_total = 0  
    while True:
        item_input = input(f"What would you like to buy? (type 'done' to finish): ").lower()
        if item_input == "done":
            break

        items = item_input.split()
        for item in items:
            if item not in menu:
                print(f"Sorry, {item} is not on the menu.")
                continue

            qty = input(f"How many {item.title()}? ")
            if not qty.isdigit():
                print("Please enter a valid number.")
                continue

            qty = int(qty)
            price = menu[item]
            total = price * qty

            
            if total >= 200:
                total *= 0.9

            receipt.append(f"{customers} - {item.title()} x{qty} = ₹{total:.2f}")
            customer_total += total

    print(f"{customers}, Your total is ₹{customer_total:.2f}")
    grand_total += customer_total

print("\nReceipt:")
for line in receipt:
    print(line)

print(f"Customers are Done. Total sales today: ₹{grand_total:.2f}")
