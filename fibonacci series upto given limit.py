#FIBONACCI SERIES UPTO GIVEN LIMIT

limit = int(input("Enter a limit to stop the series:"))

pos1 = 0
pos2 = 1
limit_track = 2
print(pos1)
print(pos2)
for i in range(2,limit):
    #fibonacci series means current number and previous number added to give the next number
    pos3 = pos1 + pos2
    pos1 = pos2
    pos2 = pos3
    print(pos3)

#fibonacci series found
