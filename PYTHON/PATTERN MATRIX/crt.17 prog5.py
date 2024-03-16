for i in range(1,5):
    for j in range(1,5):
        if(i==1 or i==4 or j==1 or j==4):
            print("x",end="")
        else:
            print(" ",end="")
    print()


count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end="")
        count=count+1
    print("")
            
