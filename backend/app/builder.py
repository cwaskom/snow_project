import datetime

def build_weather(data):
    clean_weather = [
        {"date":datetime.datetime.fromtimestamp(elem['dt']).strftime('%m-%d-%Y %H:%M:%S'), 
        "weather":elem["weather"][0]["id"],
        "description":elem["weather"][0]["description"], 
        "temp":elem["main"]["temp"], 
        "pop":elem["pop"]} 
        for elem in data]
    return clean_weather

def find_snow(clean_weather):
    snow_days = [i for i in clean_weather if i['weather'] >= 600 and i['weather'] < 700]
    return snow_days