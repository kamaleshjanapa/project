n=int(input("enter a number:"))
n1=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==n1):
    print("yes")
else:
    print("no")

