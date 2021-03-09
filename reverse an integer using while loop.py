#REVERSE AN INTEGER USING WHILE LOOP

number=int(input("Enter an integer to reverse: "))
if number<0:
    number*=(-1)
    flag=1
reverse=0
while(number>0):
    reminder=number%10
    reverse=(reverse*10)+reminder
    number=number//10
if flag==1: # integer -123 will be as -321
    print(-reverse)
else:
    print(reverse)

#integer is reversed
