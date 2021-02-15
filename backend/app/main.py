from client import Client
from builder import build_weather, find_snow
from pretty_html_table import build_table
from send_email import send_email
import pandas as pd

def run():
    # Initializses a client, calls OpenWeather API 5-Day forecast and returns a list of dictionaries of weather details
    weather = Client()
    data = weather.request_weather()

    # Cleans weather data and returns only elements with snow in the forecast 
    clean_weather = build_weather(data)
    snow_days = find_snow(clean_weather)

    # Convert snow days data to Panda's DataFrame
    df = pd.DataFrame(snow_days)

    # Checks if snow in the forecast. If not, don't send an email
    if df.empty:
        print("No snow")
    else: 
        # Convert DataFrame to pretty html table
        output = build_table(df, 'blue_light')

        # Email weather forecast
        send_email(output)
        return "Mail sent succesfully"

if __name__ == "__main__":
    run()