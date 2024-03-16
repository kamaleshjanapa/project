
#lambda function
b=lambda x,y:x**y
print(b(2,3))
a=lambda x : x+10
print(a(5))

print()
#map function
#c=map(function,iterablevalue)
l1=[23,45,156,186]
c=list(map(lambda x:x//10,l1))
print(c)
c=list(map(lambda x:x//10,[23,45,156,186]))
print(c)

def check(n):
    if n%2==0:
        print("yes")
    elif (n+1)%2==0:
        print("no")
    else:
        print("enter again")
a=map(check,[2,3,471,12,13])
b=list(a)
print(b)

