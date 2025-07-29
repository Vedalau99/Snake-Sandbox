guest = input("How many people?")
guest = int(guest)

for i in range(guest):
    name = input("Enter your name ")
    age = input("Enter your age ")
    age = int(age) 
    if age<13:
        demo = "you are a child!"
    elif 13<=age<18:
        demo = "you are a teenager!"
    else:
        demo = "You are an adult!"

    print(f"{i+1}.Hello {name},{demo}\n")



