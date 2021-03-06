#FACTORIAL OF A NUMBER USING FOR LOOP

number=int(input("Enter a number:"))
factorial = 1
#factorial of 0 and 1 is 1. And no factorial for negative numbers

if(number<0):
    print("There exists no factorial for negative numbers.")
elif(number==0):
    print("Factorial is 1")
#for example, factorial of 2 means 2*1, 3 means 3*2*1
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("Factorial is",factorial)

#Factorial of the number is found
    
