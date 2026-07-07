fine=10000
count=0
paid=0
while fine > 0:
    payment=int(input("Enter your fine amount(0 to stop): "))
    if payment == 0:
        break
    if payment > fine:
        print("Payment exceeds remaining fine")
    else:
        fine -= payment
        count += 1
        paid += payment
print("Number of payments made: ",count)
print("Total amount paid: ",paid)
print("Remaining fine: ",fine)
    
    
