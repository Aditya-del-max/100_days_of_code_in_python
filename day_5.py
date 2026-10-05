#add 1 to 100

y=int(input("enter numbers less than 100 "))
while y>100:
    y=int(input("enter numbers less than 100 "))
total=0
for number in range(1, y+1, 2):
    total += number

print(total)
i=int(1)
j=int(100)
grand_total=0
k=0
while k<50:
    total= int(i)+int(j)
    grand_total+=total 
    i+=1
    j-=1
    k+=1
print(grand_total)
