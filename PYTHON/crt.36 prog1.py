#22,-1,42,65,1,-4,6
#write a program to find the second smallest negative number from the list without using sort,min and max
a=[22,11,42,45,65,1,-4,-1]
m1=100
m2=100
for i in a:
    if i<m1:
        m2=m1
        m1=i
    elif m2>i and m2>m1:
        m2=i
print(m2)
