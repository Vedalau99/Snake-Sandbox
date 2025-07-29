grand_total = 0 
receipt = []
customers = input("how many customers?  ")
customers =int(customers)
menu = ["chips", "cookies", "juice"]
prices = [10, 15, 20]
menu_prices = dict(zip(menu, prices))

while (customers)!=0:
    customers = customers -1
    name = input("Enter your name  ")
    item = input(f"what would you like to buy,{menu}")
    Qty = input("how many? ")
    Qty = int(Qty)
    price = menu_prices[item]
    total = price * Qty
    Order= (f"{name},your total is ${total}")
    receipt.append(f"{name} - {item} x{Qty} = ₹{total}")
    print(Order)
    grand_total += total
print("Receipt:")
for line in receipt:
    print(line)
print(f"All purchases complete. Total sales today: ₹{grand_total}")

