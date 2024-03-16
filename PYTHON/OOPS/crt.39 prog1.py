class Faculty:
    def __init__(self,f_name,dpartment,f_id):
        self.f_name=f_name
        self.dpartment=dpartment
        self.f_id=f_id
    def print_info(self):
        print("faculty information:",self.f_name,self.dpartment,self.f_id)
obj=Faculty("joker","computer_science",21586)
obj.print_info()

class cse(Faculty):
    pass
obj=cse("don","computer_science",21587)
obj.print_info()


'''#create a class of name placements
#which have a function info which displayes "no of placements 675 still counting"
#create another class of name dpartment
#with function display which displays the names of dpartments present in college
#create a class pragati with a function welcome which displays the message "welcome to pragati engineering college we grat to have you"
#pragati class should also displaythe details about dpartment and placements
# multilevel
class Placements:
    def info(self):
        print("623")
class dpartment(Placements):
    def display(self):
        print("all depts")
class pragati(dpartment):
    def welcome(self):
        print("welcome")
obj=pragati()
obj.info()
obj.display()
obj.welcome()
'''

'''class Arthimetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(a,b,c):
        print(a,b,c)
obj=Arthimetic()
obj.add(5)
obj.add(5,6)
obj.add(5,6,7)'''


class father():
    def bike(self):
        print("bentley")
    def laptop(self):
        print("2 gb laptop")
class son(father):
    def laptop(self):
        print("not sufficient")
obj=son()
obj.bike()
obj.laptop()






























