import time
from ibus import IBus
import gps

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

while True:
    print("Pętla")
# Obsługa aparatury sterującej
    # Odczyt z odbiornika i zapis do listy kanałów
    try:
        res = ibus_in.read()
        if (res[0] == 1):
            print (IBus.normalize(res[2]))
            
        else:
            print ("Status offline {}".format(res[0]))
            #time.sleep(0.5)
    except IOError as e:
        print(f"Wystąpił błąd: {e}")
#Obsługa modułu GPS
'''
    try:
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
'''