import json
import requests
import time

# API key and San Francisco coordinates
APIKey = "f71aa985b19972050320f443f38c43c9"
CityLat = "37.7790262"
CityLon = "-122.419906"

# API URL
APICall = f"https://api.openweathermap.org/data/2.5/weather?lat={CityLat}&lon={CityLon}&appid={APIKey}"

# Simulated ports (for demonstration only)
Thermostat_Port = 0
LCD_Port = 9

# Status codes
OFF = 0
COOLING = 1
HEATING = 2

def getFahrenheit(temp_k):
    return int((temp_k - 273.15) * 9 / 5 + 32)

def getCelsius(temp_k):
    return int(temp_k - 273.15)

def getHumidity(humidity):
    return str(humidity)

def simulateCustomWrite(port, message):
    print(f"[PORT {port}] {message}")

def process_weather_data(data):
    city_weather = data
    current_temp = city_weather["main"]["temp"]
    current_humidity = city_weather["main"]["humidity"]

    fahrenheit = getFahrenheit(current_temp)
    celsius = getCelsius(current_temp)
    humidity = getHumidity(current_humidity)

    print(f"Temperature: {fahrenheit}°F / {celsius}°C")
    print(f"Humidity: {humidity}%")

    # Decision logic
    if celsius >= 28:
        print("AC is ON.")
        simulateCustomWrite(Thermostat_Port, "COOLING MODE")
        simulateCustomWrite(LCD_Port, f"{fahrenheit}°F | {celsius}°C | {humidity}%\nAC is ON.")
    elif celsius <= 15:
        print("Heater is ON.")
        simulateCustomWrite(Thermostat_Port, "HEATING MODE")
        simulateCustomWrite(LCD_Port, f"{fahrenheit}°F | {celsius}°C | {humidity}%\nHeater is ON.")
    else:
        print("Temperature is optimal. System is OFF.")
        simulateCustomWrite(Thermostat_Port, "OFF")
        simulateCustomWrite(LCD_Port, f"{fahrenheit}°F | {celsius}°C\nHumidity: {humidity}%")

def main():
    while True:
        print("\n🔄 Fetching weather data...\n")
        try:
            response = requests.get(APICall)
            if response.status_code == 200:
                weather_data = response.json()
                process_weather_data(weather_data)
            else:
                print(f"Failed to fetch weather data: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

        # Wait for 1 hour before checking again
        time.sleep(3600)

if __name__ == "__main__":
    main()
