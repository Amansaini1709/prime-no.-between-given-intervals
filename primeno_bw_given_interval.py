#prime no. in given intervals
a=int(input("enter the first interval"))
b=int(input("enter the second interval"))
for i in range(a,b,1):
    for d in range (2,i,1):
        if i%d=0:
            break
    else:
        print (i)
