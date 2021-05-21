# For loop
list=["HARRY","LARRY","CARRY","MARIE"]
for items in list:
    print(items)

# While loop
i=0
while (i<45):
    print(i)
    i=i+1

#or
i=0
while(True):
    print(i+1, end=" ")
    if (i==44):
     break
    i=i+1

# Break & Continue Statement
i= 0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        break
    i =i+1

