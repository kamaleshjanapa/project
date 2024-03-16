a=int(input("enter the price :"))
if a>72000 & a>150000:
      print("then income taxes is 10% then insurance will be 15% of the actual price")
elif a>150000 & a>200000:
    print("the tax will be 25% and insurance will be 20%")
elif a>200000:
    print("tax will be 35% and insurance will be 25%")
else:
    print("minimum price with us 75000 valid value")
    
