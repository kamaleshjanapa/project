# write a login function
#which accepts the user only when the username and password are same
#and displaced the message login succesfull otherwise it keeps asking the user to enter the message untill it was correct
def login():
    while True:
        username=input("enter the username:")
        password=input("enter the password:")
        if(username==password):
            print("login successfull")
            break
        else:
            print("login unsucessfull")
login()
