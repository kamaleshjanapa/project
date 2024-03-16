a=int(input("enter a number :"))
if a%3==0 & a%6==0:
    print("good number")
elif a%2==0 & a%7==0:
    print("average number")
elif a%4==0 & a%9==0:
    print("awesome number")
else:
    print("bad number")
    
#another method nested if
    a=int(input("enter a number :"))
if a%3==0:
    if a%6==0:
        print("good number")
