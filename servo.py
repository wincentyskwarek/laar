import RPi.GPIO as GPIO
import time 
# use P1 header pin numbering convention
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)
pwm = GPIO.PWM(22,50)
pwm.start(2)
time.sleep(1)
while True:
    i=0
    while i<100:
        pwm.ChangeDutyCycle(float(i))	
        time.sleep(1)
        print(i)
        i+=1
     

pwm.stop()
GPIO.cleanup()
print ("Konic")