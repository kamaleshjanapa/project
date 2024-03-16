a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))     
if a == b == c:
      print("Equilateral Triangle")
elif a == b or a == c or b == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
