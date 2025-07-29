guests = input("How many guests? ")
guests = int(guests)
for i in range (guests):
         name = input("Enter your name ") 
         age = input("Enter your age ")
         age = int(age)    
         if age <18:
                   invite = f"Sorry {name}, you're too young to attend"
                   print(invite)
         else:
                   invite = f"Welcome to the party, {name}!"
                   print(invite)
print("Guest list check Complete!")




