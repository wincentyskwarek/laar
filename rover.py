from math import *
import RPi.GPIO as GPIO


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
        angle+=100
        #self.wheel26p.ChangeDutyCycle(100)
        b=100
        # Odległość od środka łazika do środka koła szerokość
        x=41.25
        # Odległość od środka łazika do środka koła długość
        y=64
        r=b/(2*tan(angle))
        alpha1=atan(y/(r-x))
        alpha2=atan(y/(r+x))
        r1=sqrt((r-x)**2+y**2)
        r2=sqrt((r+x)**2+y**2)
        ra=sqrt(r**2+(b/2)**2)
        alpha1=(alpha1*7.2)/90
        alpha2=(alpha2*7.2)/90
        omega=speed/r
        speed15=omega*r1
        speed3=omega*(r-24.5)
        speed4=omega*(r+24.5)
        speed26=omega*r2

        
        print(angle, speed, speed15, speed26, speed3, speed4, alpha1, alpha2) 
        if speed<5 and speed>-5:
            speed=0

        

@staticmethod
def normalize (value):
    return 0
