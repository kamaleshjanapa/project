n=12345
while(n>0):
    digit=n%10
    print(digit)
    n=n//10


print()
c=0
n=12345
while(n>0):
    digit=n%10
    n=n//10
    c=c+1
    print(c)



print()
s=0
n=12345
while(n>0):
    digit=n%10
    s=s+digit
    n=n//10
    print(s)


print()
m=1
n=12345
while(n>0):
    digit=n%10
    m=m*digit
    n=n//10
    print(m)
