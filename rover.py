import math
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
        angle=(angle+100)//2
        speed=(speed+100)//2
        self.wheel15t.ChangeDutyCycle(speed)
        self.wheel3t.ChangeDutyCycle(speed)
        self.wheel26t.ChangeDutyCycle(speed)
        self.wheel4t.ChangeDutyCycle(speed)
        self.servo1.ChangeDutyCycle(angle)
        self.servo2.ChangeDutyCycle(angle)
        self.servo5.ChangeDutyCycle(angle)
        self.servo6.ChangeDutyCycle(angle)

        # Wheel 1 and wheel 5
        
        #angle1=int(angle1*Rover.servoAngle)//100
        #self.k15.ChangeDutyCycle(abs(angle1))
        # Wheel 2 and wheel 6
       
        #angle1=int(angle2*Rover.servoAngle)//100
        #self.k26.ChangeDutyCycle(abs(angle2))
        # Wheel 3
        
        # Wheel 4
        
#    print((angle, angle2, angle3, angle4, angle5, angle6) )
@staticmethod
def normalize (value):
    return 0
