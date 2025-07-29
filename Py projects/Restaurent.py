grand_total = 0 
receipt = []

customers = input("how many customers?  ")
customers = int(customers)
menu = {
    "idli": 10,
    "vada": 15,
    "dosa": 25,
    "tea": 8,
    "coffee": 12
}


while (customers)!=0:
    customers = customers -1
    name = input("Enter your name  ")
    item = input(f"What would you like to buy? {list(menu.keys())}: ").lower()
    Qty = input("how many?  ")



    if item not in menu:
        print("Sorry, item not on menu.")
        continue


    Qty =int(Qty)
    price = menu[item]

    if Qty < 3:
        price = price
    else:
        price = price * 0.9

    
    total = price * Qty      
    Order =f"{name},Your total is ${total:.2f}"
    
    
    receipt.append(f"{name} - {item} x{Qty} = {total:.2f}")
    print(Order)
    grand_total += total



print("\nReceipt:")
for line in receipt:
    print(line)
print(f"All orders fulfilled. Total sales today: {grand_total:.2f}")