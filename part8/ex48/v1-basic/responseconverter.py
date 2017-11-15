from weatherinfo import WeatherInfo

def parse_response(jsonresponse):
    weather = jsonresponse["weather"]
    weather_data = weather[0]
    description = weather_data["description"]
    main_data = jsonresponse["main"]
    temp_kelvin = float(main_data["temp"])
    sys_data = jsonresponse["sys"]
    sunrise = int(sys_data["sunrise"])
    sunset = int(sys_data["sunset"])
    name = jsonresponse["name"]

    weatherinfo = WeatherInfo(name, description, temp_kelvin, sunrise, sunset)
    return weatherinfo
