#TO CHECK GIVEN INTEGER IS PALINDROME OR NOT

give_number=int(input("Enter an integer to check for palindrome: "))
number = give_number
reverse=0
while(number>0):
    reminder=number%10
    reverse=(reverse*10)+reminder
    number=number//10
if give_number==reverse:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")

#palindrome check done
