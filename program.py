import time
from ibus import IBus
from rover import Rover
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
#Definicja pinów łazika
LPrzodTyl = 4       # Silnik koła lewego przód i tył
PPrzodTyl = 17      # Silnik koła lewego przód i tył
LSrodek = 27        # Silnik koła lewego środek
PSrodek = 22        # Silnik koła prawego środek
LKatPrzod = 10   # Servo koła lewego przód i tył
PKatPrzod = 9    # Servo koła prawego przód i tył
LKatTyl = 11   # Servo koła lewego przód i tył
PKatTyl = 23    # Servo koła prawego przód i tył
DirectionPin = 24   # Pin kierunku ruchu silników
OdbiornikPinRX = 25 # Pin odbiornika aparatury sterującej
GPSTXPin = 12       # Pin RXD od odbiornika GPS
GPSRXPin = 13       # Pin TXD od odbiornika GPS

#Definicja obiektu klasy lazik
lazik = Rover(LPrzodTyl, PPrzodTyl, LSrodek, PSrodek, LKatPrzod, PKatPrzod, LKatTyl, PKatTyl, DirectionPin)

while True:
# Obsługa aparatury sterującej
    # Odczyt z odbiornika i zapis do listy kanałów
    res = ibus_in.read()
    if (res[0] == 1):
        kat=IBus.normalize(res[2])
        predkosc=IBus.normalize(res[3])
        lazik.go(kat,predkosc)
        #print(predkosc)
        
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
