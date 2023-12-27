import time
from ibus import IBus
import gps
import RPi.GPIO as GPIO


#Uruchomienie IBUS
ibus_in = IBus()

# Utworzenie sesji GPS
session = gps.gps(mode=gps.WATCH_ENABLE)

#res[0],    # Status
#IBus.normalize(res[1]),
#IBus.normalize(res[2]),
#IBus.normalize(res[3]) - prędkość
#IBus.normalize(res[4]),
#IBus.normalize(res[5], type="dial"),
#IBus.normalize(res[6], type="dial")),
#definicja pinu GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
#GPIO.output(4, GPIO.HIGH)

pwm = GPIO.PWM(4,100 )
pwm.start(100)

while True:
# Obsługa aparatury sterującej
    # Odczyt z odbiornika i zapis do listy kanałów
    res = ibus_in.read()
    if (res[0] == 1):
        kat=IBus.normalize(res[2])
        predkosc=IBus.normalize(res[3])
        print(predkosc)
        predkosc=max(-1*predkosc, predkosc)
        pwm.ChangeDutyCycle(predkosc)
    else:
        print ("Status offline {}".format(res[0]))

#Obsługa modułu GPS
    try:
        if session.waiting():  # Sprawdza, czy są dostępne nowe dane
            report = session.next()
            # Czekaj na raporty TPV (Time Position Velocity)
            if report['class'] == 'TPV':
                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                    print("Latitude: ", report.lat)
                    print("Longitude: ", report.lon)

    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
#pwm.stop()
GPIO.cleanup()
