# write a function which takes 2 parameters (arguments) a and b
#typecast the value of 2nd argument into integer
#then multiply the both the arguments then print the last digit of the result
def name(a,b):
    b=int(b)
    result=a*b
    name=result%10
    print(name)
name(11,12)#position arguments

print()
#keyword arguments
def name(a,b):
    b=int(b)
    result=a*b
    name=result%10
    print(name)
name(b=25,a=2)

print()
#default argument
def check(name,place):
    print("my name is",name,"i am from",place)
check(place="kakinada",name="kamalesh")

print()
#unknown argument
def func(**name):
    print("my name is ",name["fname"],name["lname"])
func(fname="kamalesh",lname="janapa")

    
    
