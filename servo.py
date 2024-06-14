import RPi.GPIO as GPIO
import time 
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

GPIO.setup(22,GPIO.OUT)
pwm = GPIO.PWM(22,50)
pwm.start(2)
time.sleep(1)

try:
    dane = -1

    while (dane != "0"):			
        dane = int(input("Wprowadz cyfre:"))		
        pwm.ChangeDutyCycle(float(dane))	
        time.sleep(.03)


except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

pwm.stop()
GPIO.cleanup()
print ("Konic")