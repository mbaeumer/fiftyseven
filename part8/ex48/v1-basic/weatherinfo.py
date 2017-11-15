import datetime
class WeatherInfo:
    def __init__(self, name, description, temp, sunrise, sunset):
      self.name = name
      self.description = description
      self.temp_kelvin = temp
      self.temp_celsius = self.temp_kelvin - 273.15
      self.sunrise = datetime.datetime.fromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
      self.sunset = datetime.datetime.fromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')