from math import *
import RPi.GPIO as GPIO
import time


class Rover():
    a=0.5               # Rozstaw kół [m]
    b=1                 # Rozstaw osi [m]
    servoAngle = 180    # Maksymalny kąt obrotu serwa
    maxSpeed = 0.5      # Maksymalna prędkość z obliczeń 316
    def __init__(self, w15p, w15t, w3p, w3t, w26p, w26t, w4p, w4t, k1, k5, k2, k6, ActivePin):
        self.frequency = 100 #częstotliwość PWM
        self.servoFrequency = 50 #częstotliwość PWM
        self.ActivePin=ActivePin
        GPIO.setmode(GPIO.BCM) #Używane nazwy pinów można też dać GPIO.setmode(GPIO.BOARD)
        
        #Definicja kol
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
        GPIO.output(k1, True)
        GPIO.output(k2, True)
        GPIO.output(k5, True)
        GPIO.output(k6, True)
        # Inicjalizacja pinów

        self.wheel15p = GPIO.PWM(w15p,self.frequency)
        self.wheel15t = GPIO.PWM(w15t,self.frequency)
        self.wheel3p = GPIO.PWM(w3p,self.frequency)
        self.wheel3t = GPIO.PWM(w3t,self.frequency)
        self.wheel26p = GPIO.PWM(w26p,self.frequency)
        self.wheel26t = GPIO.PWM(w26t,self.frequency)
        self.wheel4p = GPIO.PWM(w4p,self.frequency)
        self.wheel4t = GPIO.PWM(w4t,self.frequency)
        self.servo1 = GPIO.PWM(k1,self.servoFrequency)
        self.servo2 = GPIO.PWM(k2,self.servoFrequency)
        self.servo5 = GPIO.PWM(k5,self.servoFrequency)
        self.servo6 = GPIO.PWM(k6,self.servoFrequency)
        
        self.wheel15p.start(0)
        self.wheel15t.start(0)
        self.wheel3p.start(0)
        self.wheel3t.start(0)
        self.wheel26p.start(0)
        self.wheel26t.start(0)
        self.wheel4p.start(0)
        self.wheel4t.start(0)
        self.servo1.start(0)
        self.servo2.start(0)
        self.servo5.start(0)
        self.servo6.start(0)

    def go(self, angle, speed):
        if speed<5 and speed>-5:
            speed=0
        angle*=0.8
        #self.wheel26p.ChangeDutyCycle(100)
        b=1
        # Odległość od środka łazika do środka koła szerokość
        x=0.4125
        # Odległość od środka łazika do środka koła długość
        y=0.64
        if speed > 99 or speed == 99:
            speed=99
        if speed < -99 or speed == -99:
            speed= -99
        if angle!=0:
            r=b/(0.5*tan(radians(angle)))
            alpha1=degrees(atan(y/(r-x)))
            alpha2=degrees(atan(y/(r+x)))
            r1=sqrt((r-x)**2+y**2)
            r2=sqrt((r+x)**2+y**2)
            ra=sqrt(r**2+(b/2)**2)
            alpha1=(alpha1*7.2)/90
            alpha2=(alpha2*7)/90
            omega=speed/r
            speed15=omega*r1
            speed3=omega*(r-24.5)
            speed4=omega*(r+24.5)
            speed26=omega*r2
        else:
            alpha1=(angle*7.2)/90
            alpha2=(angle*7.2)/90
            speed15=0.0002*speed
            speed3=0.0002*speed
            speed4=0.0002*speed
            speed26=0.0002*speed
            r=1000
        
        if speed>0:
            self.wheel15p.ChangeDutyCycle(speed15)
            self.wheel3p.ChangeDutyCycle(speed3)
            self.wheel26p.ChangeDutyCycle(speed26)
            self.wheel4p.ChangeDutyCycle(speed4)
            self.wheel15t.ChangeDutyCycle(0)
            self.wheel3t.ChangeDutyCycle(0)
            self.wheel26t.ChangeDutyCycle(0)
            self.wheel4t.ChangeDutyCycle(0)                       
        else:
            speed15=-speed15
            speed26=-speed26
            speed3=-speed3
            speed4=-speed4
            self.wheel15t.ChangeDutyCycle(speed15)
            self.wheel3t.ChangeDutyCycle(speed3)
            self.wheel26t.ChangeDutyCycle(speed26)
            self.wheel4t.ChangeDutyCycle(speed4)
            self.wheel15p.ChangeDutyCycle(0)
            self.wheel3p.ChangeDutyCycle(0)
            self.wheel26p.ChangeDutyCycle(0)
            self.wheel4p.ChangeDutyCycle(0)

        self.servo1.ChangeDutyCycle(7.5-alpha1)
        self.servo2.ChangeDutyCycle(7.2-alpha2)
        
        self.servo5.ChangeDutyCycle(7.2+alpha1)
        self.servo6.ChangeDutyCycle(7+alpha2)
        


        
        

@staticmethod
def normalize (value):
    return 0
