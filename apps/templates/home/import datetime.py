import datetime
from astral.sun import sun

# Latitude and longitude of Montreal
LATITUDE = 45.5017
LONGITUDE = -73.5673

def get_sunrise_sunset_times(date):
    city_sun = sun(LATITUDE, LONGITUDE, date=date)
    return city_sun["sunrise"], city_sun["sunset"]

def main():
    current_date = datetime.datetime.now().date()
    
    sunrise, sunset = get_sunrise_sunset_times(current_date)
    
    print("Today's sunrise:", sunrise)
    print("Today's sunset:", sunset)
    
    while True:
        current_time = datetime.datetime.now().time()
        
        if current_time >= sunrise.time() and current_time <= sunset.time():
            # Perform your function here for daytime
            print("Performing daytime function...")
        else:
            # Perform your function here for nighttime
            print("Performing nighttime function...")
        
        # Wait for some time before checking again (e.g., 5 minutes)
        datetime.datetime.now() + datetime.timedelta(minutes=5)

if __name__ == "__main__":
    main()
