import math
import RPi.GPIO as GPIO

class Rover():
    a=0.5               # Rozstaw kół [m]
    b=1                 # Rozstaw osi [m]
    servoAngle = 180    # Maksymalny kąt obrotu serwa
    maxSpeed = 1      # Maksymalna prędkość z obliczeń 316
    def __init__(self, w15p, w15t, w3p, w3t, w26p, w26t, w4p, w4t, k1, k5, k2, k6, ActivePin):
        self.frequency = 100 #częstotliwość PWM
        self.ActivePin=ActivePin
        GPIO.setmode(GPIO.BCM) #Używane nazwy pinów można też dać GPIO.setmode(GPIO.BOARD)
        #Definicja pinów kół
        GPIO.setup(w15p, GPIO.OUT)
        GPIO.setup(w15t, GPIO.OUT)
        GPIO.setup(w3p, GPIO.OUT)
        GPIO.setup(w3t, GPIO.OUT)
        GPIO.setup(w26p, GPIO.OUT)
        GPIO.setup(w26t, GPIO.OUT)
        GPIO.setup(w4p, GPIO.OUT)
        GPIO.setup(w4t, GPIO.OUT)
        GPIO.setup(k1, GPIO.OUT)
        GPIO.setup(k2, GPIO.OUT)
        GPIO.setup(k5, GPIO.OUT)
        GPIO.setup(k6, GPIO.OUT)
        # Definicja pinów kierunku
        GPIO.setup(ActivePin, GPIO.OUT)
        GPIO.output(ActivePin, GPIO.HIGH)
        # Inicjalizacja pinów
        self.wheel15p = GPIO.PWM(w15p,self.frequency)
        self.wheel15t = GPIO.PWM(w15t,self.frequency)
        self.wheel3p = GPIO.PWM(w3p,self.frequency)
        self.wheel3t = GPIO.PWM(w3t,self.frequency)
        self.wheel26p = GPIO.PWM(w26p,self.frequency)
        self.wheel26t = GPIO.PWM(w26t,self.frequency)
        self.wheel4p = GPIO.PWM(w4p,self.frequency)
        self.wheel4t = GPIO.PWM(w4t,self.frequency)
        self.servo1 = GPIO.PWM(k1,self.frequency)
        self.servo2 = GPIO.PWM(k2,self.frequency)
        self.servo5 = GPIO.PWM(k5,self.frequency)
        self.servo6 = GPIO.PWM(k6,self.frequency)
        self.wheel15p.start(0)
        self.wheel15t.start(0)
        self.wheel3p.start(0)
        self.wheel3t.start(0)
        self.wheel26p.start(0)
        self.wheel26t.start(0)
        self.wheel4p.start(0)
        self.wheel4t.start(0)

    def go(self, angle, speed):
        #self.wheel26p.ChangeDutyCycle(100)
        if angle!=0:
            r=Rover.b/(2*math.sin(angle))
            omega=speed/r
            #Wheel 1
            angle1=math.atan(Rover.b/(2*(r-Rover.a/2)))
            r1=Rover.b/(2*math.sin(angle1))
            speed1=omega*r1
            #Wheel 2
            angle2=math.atan(Rover.b/(2*(r+Rover.a/2)))
            r2=Rover.b/(2*math.sin(angle2))
            speed2=omega*r2
            #Wheel 3
            angle3=math.atan(0/(2*(r-Rover.a/2)))
            r3=r-Rover.a/2
            speed3=omega*r3
            #Wheel 4
            angle4=math.atan(0/(2*(r+Rover.a/2)))
            r4=r+Rover.a/2
            speed4=omega*r4
            #Wheel 5
            angle5=-math.atan(Rover.b/(2*(r-Rover.a/2)))
            r5=-Rover.b/(2*math.sin(angle5))
            speed5=omega*r5
            #Wheel 6
            angle6=-math.atan(Rover.b/(2*(r+Rover.a/2)))
            r6=-Rover.b/(2*math.sin(angle6))
            speed6=omega*r6
        else:
            speed1=speed
            speed2=speed
            speed3=speed
            speed4=speed
        if speed>0:
            print("")
            #self.wheel15p.ChangeDutyCycle(abs((speed1*Rover.maxSpeed/100)//30))
            #self.wheel3p.ChangeDutyCycle(abs((speed3*Rover.maxSpeed/100)//30))
            self.wheel26p.ChangeDutyCycle(abs((speed2*Rover.maxSpeed))
            #self.wheel4p.ChangeDutyCycle(abs((speed4*Rover.maxSpeed/100)//30))
            #self.wheel15t.ChangeDutyCycle(0)
            #self.wheel3t.ChangeDutyCycle(0)
            self.wheel26t.ChangeDutyCycle(0)
            #self.wheel4t.ChangeDutyCycle(0)
        else:
            print("")
            #self.wheel15t.ChangeDutyCycle(abs((speed1*Rover.maxSpeed/100)//30))
            #self.wheel3t.ChangeDutyCycle(abs((speed3*Rover.maxSpeed/100)//30))
            self.wheel26t.ChangeDutyCycle(abs((speed2*Rover.maxSpeed))
            #self.wheel4t.ChangeDutyCycle(abs((speed4*Rover.maxSpeed/100)//30))
            #self.wheel15p.ChangeDutyCycle(0)
            #self.wheel3p.ChangeDutyCycle(0)
            self.wheel26p.ChangeDutyCycle(0)
            #self.wheel4p.ChangeDutyCycle(0)
        # Wheel 1 and wheel 5
        
        #angle1=int(angle1*Rover.servoAngle)//100
        #self.k15.ChangeDutyCycle(abs(angle1))
        # Wheel 2 and wheel 6
       
        #angle1=int(angle2*Rover.servoAngle)//100
        #self.k26.ChangeDutyCycle(abs(angle2))
        # Wheel 3
        
        # Wheel 4
        
        print(abs((speed1*Rover.maxSpeed/100)//30), abs((speed2*Rover.maxSpeed/100)//30), abs((speed3*Rover.maxSpeed/100)//30), abs((speed4*Rover.maxSpeed/100)//30) )
    @staticmethod
    def normalize (value):
        return 0
