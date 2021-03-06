#FACTORIAL OF A NUMBER USING RECURSION

#recursion part

def factorial_recursion(number):
    if number==1:
        return 1
    else:
        return number*factorial_recursion(number-1) #factorial of 5 is 5*fact(5-1)
        
number=int(input("Enter a number:"))
#factorial of 0 and 1 is 1. And no factorial for negative numbers

if(number<0):
    print("There exists no factorial for negative numbers.")
elif(number==0):
    print("Factorial is 1")
#for example, factorial of 2 means 2*1, 3 means 3*2*1
else:
    print("Factorial is",factorial_recursion(number))

#Factorial of the number is found.
    
