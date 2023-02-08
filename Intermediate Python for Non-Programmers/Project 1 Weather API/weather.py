import requests

class City:
    def __init__(self, name, lat, lon, units="metric", degree_symbol = "C"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.degree_symbol = degree_symbol
        
        self.get_data()
        
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=cdd4d6ad23e334209d5430677aeda6b4")

        except:
            print("No internet access")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        
        if self.units == "imperial":
            self.degree_symbol = "F"
        
            
        print(f"In {self.name} it is currently {self.temp} {self.degree_symbol}")
        print(f"Today's High: {self.temp_max} {self.degree_symbol}")
        print(f"Today's Low: {self.temp_min} {self.degree_symbol}")
        
my_city = City("Cincinnati", 39.1031, -84.5120) #Sometimes negative Number is required
my_city.temp_print()

print(my_city.response_json)

vacation_city = City("Portland", 45.5152, -122.6784)
vacation_city.temp_print()

tokyo = City("Tokyo", 35.6762, 139.6503)
tokyo.temp_print()

my_second_city = City("Cincinnati", 39.1031, -84.5120, "imperial")
my_second_city.temp_print()