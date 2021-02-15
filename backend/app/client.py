import requests

class Client:
    API_KEY = "38f307611e4a387b4f6a7f5976446f58"
    LAT = "41.3497"
    LON = "72.0791" 
    URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=imperial"
    
    def request_weather(self):
        response = requests.get(self.URL)
        data = response.json()['list']
        return data