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
    def time(self,start_time,end_time):
        print("class start time:",start_time,end_time)
        self.sc=start_time
        self.ec=end_time
    def display(self):
        diff = self.ot-self.it
        print(diff)
        print(self.sp)
        print(self.sc)
        print(self.ec)
joker=F15()
joker.lights("white")
joker.fan(5)
joker.ac(16.0,45.0)
joker.time(9,4)
joker.display()


