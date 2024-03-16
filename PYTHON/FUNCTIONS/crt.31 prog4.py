#write a recursive model to print the number in reverse order
def reverse(number):
    if(number==0):
        return
    else:
        print(number % 10,end="")
        reverse(number//10)
reverse(12345)
print()


print()
#write aa recursive function to calculate the no of digits of a number
def recv(n):
    if n<10:
        return 1
    else:
        return 1+recv(n//10)
print(recv(12345))
print()


print()
#write aa recursive function to calculate the sum of digits of a number
def recv(n):
    if n<10:
        return n
    else:
        r=n%10
        return r+recv(n//10)
print(recv(12345))
print()


        
