#create a class with functions light,fan,and ac
#when light function is called it prints out the colour ofthe light ,which is taken as parameter to the function
#when fan function is called it is placed at the speedor that displays the regulators speed , find the function
#ac displays the room temperature and outside temperatue which are take as parameter
#write a fourth function whose name is displays the difference b/w outside temperature and room temperature
class F15:
    def __init__(self):
        print("the number of placements 550 still counting:")
        a=10
        b=23.4
        print(a+b)
    def lights(self,color):
        print("color is:",color)
    def fan(self,speed):
        print("speed of a fan is:",speed)
        self.sp=speed
    def ac(self,in_temp,out_temp):
        print("room temp of outside and inside:",in_temp,out_temp)
        self.it=in_temp
        self.ot=out_temp
    def display(self):
        diff = self.ot-self.it
        print(diff)
        print(self.sp)
joker=F15()
joker.lights("white")
joker.fan(5)
joker.ac(16.0,45.0)
joker.display()


#def __init__(self):#constructor , no need to call
        
