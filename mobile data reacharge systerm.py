data = 100
total = 0
count = 0
while data > 0:
    package = float(input("Enter your data(GB) amount(-1 to stop): "))
    if package == -1:
        break
    if data >= package:
        data -= package
        total += package 
        count += 1
    else:
        print("Not enough data available")
print ("Total number of successful data usages: " ,count)
print("Total data used: ",total)
print("Remaining data: " ,data)

    
    
