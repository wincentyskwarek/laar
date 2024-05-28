import gps

# Utworzenie sesji GPS
session = gps.gps(mode=gps.WATCH_ENABLE)

while True:
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
import gps

# Utworzenie sesji GPS
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
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
