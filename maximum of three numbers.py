#MAXIMUM OF THREE NUMBERS

number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
number3 = int(input("Enter number3:"))

#comparig using if loop

if(number1 >= number2 and number1 >= number3):
    print("number1 is maximum,the value is",number1)
elif(number2 >= number1 and number2 >= number3):
    print("number2 is maximum,the value is",number2)
else:
    print("number3 is maximum,the value is",number3)

#maximum of three numbers is found    
