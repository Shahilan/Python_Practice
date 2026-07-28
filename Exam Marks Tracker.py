count=0
total=0
highest=0
lowest=100
avg=0
while True:
           mark=int(input("Enter your mark(-1 to stop): "))
           if mark == -1:
               break
           if mark < 0 or mark > 100:
                                     print("Invalid mark")
                                     
           else:
               count += 1
               total += mark
               avg = total/count

               if mark > highest:
                   highest = mark
               if mark < lowest:
                   lowest = mark

print("Number of valid marks:", count)
print("Total marks:", total)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", avg)
                   

               
               
               
               

 
