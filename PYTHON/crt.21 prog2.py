n=int(input("enter a number:"))
s=0
for i in range(1,int( n/2+1)):
    if  (n% i == 0):
        s =s+i
if(s>n):
    print("yes")
else:
    print("no")



