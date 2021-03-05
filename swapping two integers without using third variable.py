#SWAPPING TWO INTEGERS WITHOUT USING THIRD VARIABLE
#If integer1=7 and integer2=6, after swapping integer1=6 and integer2=7 

integer1 = int(input("Enter integer1:"))
integer2 = int(input("Enter integer2:"))

print("integer1 before swapping:",integer1)
print("integer2 before swapping:",integer2)

#after swapping the value of integer1 should be in integer2 and vice versa

swap_integer1 = integer1-integer1+integer2
swap_integer2 = integer2-integer2+integer1

#Mathematically a-a+b=b

print("integer1 after swapping:",swap_integer1)
print("integer2 after swapping:",swap_integer2)

#the values are now swapped
