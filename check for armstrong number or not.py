#CHECK FOR ARMSTRONG NUMBER OR NOT

get_num=int(input("Enter a number to check armstrong number or not: "))
num = str(get_num)
sum_check = 0
for i in num:
    sum_check = sum_check + (int(i)**len(num))
if get_num==sum_check:
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")

#check for armstrong number done
