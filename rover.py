import math
class Rover():
    a=0.5
    b=1
    def __init__(self):
        return
    def go(self, angle, speed):
        self.angle=angle
        self.speed=speed
        r=b/(2*math.sin(self.angle))
        omega=self.speed/r
        #Wheel 1
        angle1=math.atan(b/(2*(r-a/2)))
        r1=b/(2*sin(angle1))
        speed1=omega*r1
        #Wheel 2
        angle2=math.atan(b/(2*(r+a/2)))
        r2=b/(2*math.sin(angle2))
        speed2=omega*r2
        #Wheel 3
        angle3=math.atan(0/(2*(r-a/2)))
        r3=r-a/2
        speed3=omega*r3
        #Wheel 4
        angle4=math.atan(0/(2*(r+a/2)))
        r4=r+a/2
        speed4=omega*r4
        #Wheel 5
        angle5=-math.atan(b/(2*(r-a/2)))
        r5=-b/(2*sin(angle5))
        speed5=omega*r5
        #Wheel 6
        angle6=-math.atan(b/(2*(r+a/2)))
        r6=-b/(2*sin(angle6))
        speed6=omega*r6


