total_stops =int(input("How many stops?  "))
passengers = 0
for stop_number in range(1,total_stops+1):
    print(f"\nstop {stop_number}")

    ON = int(input("people got on "))
    OFF = int(input("people got off "))

    passengers += ON

    if OFF > passengers:
        print("Not enough passengers to get off")
        continue
    
    passengers = passengers - OFF
    print(f"current passengers on board: {passengers}")
print(f"\nTotal passengers after final stop: {passengers}")
