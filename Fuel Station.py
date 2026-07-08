fuel=300
count=0
sold=0
while fuel > 0:
    liter=int(input("Enter fuel(liter) you want(-1 to stop): "))
    if liter == -1:
        break
    if liter <= 0:
        print("Please enter a valid amount.")
    elif liter > fuel:
        print("Not enough fuel")
    else:    
        count += 1
        fuel -= liter
        sold += liter
print("Total customers served: ",count)
print("Total liters sold: ",sold,"liter")
print("Remaining fuel: ",fuel,"liter")
