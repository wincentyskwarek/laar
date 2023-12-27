import math
import RPi.GPIO as GPIO

class Rover():
    a=0.5               # Rozstaw kół [m]
    b=1                 # Rozstaw osi [m]
    servoAngle = 180    # Maksymalny kąt obrotu serwa
    MaxSpeed = 300      # Maksymalna prędkość z obliczeń 316
    def __init__(self, w15, w26, w3, w4, k1, k2, k5, k6, dirPin):
        frequency = 100 #częstotliwość PWM
        self.dirPin=dirPin
        GPIO.setmode(GPIO.BCM) #Używane nazwy pinów można też dać GPIO.setmode(GPIO.BOARD)
        #Definicja pinów kół
        GPIO.setup(w15, GPIO.OUT)
        GPIO.setup(w26, GPIO.OUT)
        GPIO.setup(w3, GPIO.OUT)
        GPIO.setup(w4, GPIO.OUT)
        GPIO.setup(k1, GPIO.OUT)
        GPIO.setup(k2, GPIO.OUT)
        GPIO.setup(k5, GPIO.OUT)
        GPIO.setup(k6, GPIO.OUT)
        # Definicja pinów kierunku
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.output(dirPin, GPIO.LOW)
        # Inicjalizacja pinów
        self.wheel15 = GPIO.PWM(w15,frequency)
        self.wheel26 = GPIO.PWM(w26,frequency)
        self.wheel3 = GPIO.PWM(w26,frequency)
        self.wheel4 = GPIO.PWM(w26,frequency)
        self.servo1 = GPIO.PWM(k1,frequency)
        self.servo2 = GPIO.PWM(k2,frequency)
        self.servo5 = GPIO.PWM(k5,frequency)
        self.servo6 = GPIO.PWM(k6,frequency)
        self.wheel15.start(0)
        self.wheel26.start(0)
        self.wheel3.start(0)
        self.wheel4.start(0)

    def go(self, angle, speed):
        r=Rover.b/(2*math.sin(self.angle))
        omega=self.speed/r
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
        if speed>0:
            GPIO.output(self.dirPin,GPIO.HIGH)
        else:
            GPIO.output(self.dirPin,GPIO.LOW)
        # Wheel 1 and wheel 5
        self.w15.ChangeDutyCycle(abs((speed1*Rover.maxSpeed/100)//30))
        #angle1=int(angle1*Rover.servoAngle)//100
        #self.k15.ChangeDutyCycle(abs(angle1))
        # Wheel 2 and wheel 6
        self.w26.ChangeDutyCycle(abs((speed2*Rover.maxSpeed/100)//30))
        #angle1=int(angle2*Rover.servoAngle)//100
        #self.k26.ChangeDutyCycle(abs(angle2))
        # Wheel 3
        self.w3.ChangeDutyCycle(abs((speed3*Rover.maxSpeed/100)//30))
        # Wheel 4
        self.w4.ChangeDutyCycle(abs((speed4*Rover.maxSpeed/100)//30))
    @staticmethod
    def normalize (value):
        return 0
