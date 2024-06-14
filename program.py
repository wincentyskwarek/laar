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
#Silniki DC
LPrzod = 5          # Silnik koła lewego przód i tył obroty przód
LTyl = 17           # Silnik koła lewego przód i tył obroty tył
LSrodekPrzod = 26   # Silnik koła lewego środek obroty przód
LSrodekTyl = 6      # Silnik koła lewego środek obroty tył
PPrzod = 24         # Silnik koła prawego przód i tył obroty przód
PTyl = 23           # Silnik koła prawego przód i tył obroty tył

PSrodekPrzod = 16   # Silnik koła prawego środek przód
PSrodekTyl = 25      # Silnik koła prawego środek tył
#SERWA
LKatPrzod = 27   # Servo koła lewego przód i tył
LKatTyl = 18   # Servo koła lewego przód i tył
PKatPrzod = 4     # Servo koła prawego przód i tył
PKatTyl = 22    # Servo koła prawego przód i tył
ActivatePin = 20    # Pin aktywacji silnikóa
OdbiornikPinRX = 25 # Pin odbiornika aparatury sterującej
GPSTXPin = 12       # Pin RXD od odbiornika GPS
GPSRXPin = 13       # Pin TXD od odbiornika GPS

#Definicja obiektu klasy lazik
lazik = Rover(LPrzod, LTyl, LSrodekPrzod, LSrodekTyl, PPrzod, PTyl, PSrodekPrzod, PSrodekTyl, LKatPrzod, LKatTyl, PKatPrzod, PKatTyl, ActivatePin)

while True:
# Obsługa aparatury sterującej
    # Odczyt z odbiornika i zapis do listy kanałów
    res = ibus_in.read()
    if (res[0] == 1):
        kat=IBus.normalize(res[3])
        predkosc=IBus.normalize(res[1])
        lazik.go(kat,predkosc)
        print(kat)
        
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
