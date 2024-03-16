#1242,23,96,7,18,10,133 addition of minimum and maximum number 
lis=[1242,23,96,7,18,10,133]
print(lis)
min=lis[0]
max=lis[1]
minid=0
maxid=0
for i in range(len(lis)):
    if min>lis[i]:
        min = lis[i]
        minid = i

    if max<lis[i]:
        max = lis[i]
        maxid = i
s=min+max
d=max-min
lis[minid]=d
lis[maxid]=s
print(s)
print(d)
        
             
