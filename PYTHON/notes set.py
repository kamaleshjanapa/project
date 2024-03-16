#set
myset={1,2,"sanjay",6.2,"raghu","basky","sai"}
print(myset)
fs=frozenset(myset)
print(type(fs))
print(fs)



print()
a=[2,0,1024,0,40,230,0]
a2=[]
for i in a:
    if i!=0:
        a2.append(i)
print(a2)
for i in a:
    if i==0:
        a2.append(i)
print(a2)
        
