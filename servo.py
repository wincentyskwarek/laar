import RPi.GPIO as GPIO
import time
pin=27
# Ustawienia GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)  # GPIO17 jako wyjście

# Ustawienie PWM na pinie GPIO17
pwm = GPIO.PWM(pin, 50)  # 50Hz częstotliwość
pwm.start(0)  # Rozpocznij PWM z wypełnieniem 0

# Funkcja do ustawiania kąta serwa
def set_angle(angle):
    duty = 2 + (angle / 18)  # Przekształcenie kąta na cykl pracy PWM
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)  # Ustaw serwo na 0 stopni
        time.sleep(2)
        set_angle(20)  # Ustaw serwo na 20 stopni
        time.sleep(2)
        set_angle(40)  # Ustaw serwo na 40 stopni
        time.sleep(2)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()