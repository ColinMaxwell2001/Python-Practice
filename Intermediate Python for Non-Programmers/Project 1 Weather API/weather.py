import requests

class City:
    def __init__(self, name, lat, lon, units="metric", degree_symbol = "C"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.degree_symbol = degree_symbol
        
        # Called everytime a City is created
        self.get_data()
        
    def get_data(self):
        try:
            #loads in json
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=cdd4d6ad23e334209d5430677aeda6b4")

        except:
            print("No internet access")

        # puts json data into response_json variable
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]              #Extracts temp
        self.temp_min = self.response_json["main"]["temp_min"]      #Extracts temp_min
        self.temp_max = self.response_json["main"]["temp_max"]      #Extracts temp_max

    def temp_print(self):
        #Changes symbol to F when imperial
        if self.units == "imperial":
            self.degree_symbol = "F"
        
            
        print(f"In {self.name} it is currently {self.temp} {self.degree_symbol}")
        print(f"Today's High: {self.temp_max} {self.degree_symbol}")
        print(f"Today's Low: {self.temp_min} {self.degree_symbol}")


# City 1
my_city = City("Cincinnati", 39.1031, -84.5120) #Sometimes negative Number is required
my_city.temp_print()

print(my_city.response_json)

# City 2
vacation_city = City("Portland", 45.5152, -122.6784)
vacation_city.temp_print()

# City 3
tokyo = City("Tokyo", 35.6762, 139.6503)
tokyo.temp_print()

# City 4
my_second_city = City("Cincinnati", 39.1031, -84.5120, "imperial")
my_second_city.temp_print()