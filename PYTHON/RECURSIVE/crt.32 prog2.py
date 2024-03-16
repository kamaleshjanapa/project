#write the code of armstrong number using recursiveion
def count(n):
    if n<10:
        return 1
    else:
        return 1+count(n//10)
print(count(153))

def armstrong(m):
    if m==0:
        return 0
    else:
        r=m%10
        return (r**+armstrong(m//10))
print(armstrong(153))
