import requests

# Replace with your actual OpenWeatherMap API key
# API_KEY = '' #where we will put the API key
CITY = 'San Jose'
UNIT = 'metric'  # use 'imperial' for Fahrenheit

# Thresholds for thermostat control
COOLING_THRESHOLD = 26  # Degrees Celsius
HEATING_THRESHOLD = 18

def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNIT}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print("Error fetching weather data:", data)
        return None
    
    temp = data['main']['temp']
    print(f"[INFO] Current temperature in {CITY}: {temp}°C")
    return temp

def adjust_thermostat(temp):
    if temp > COOLING_THRESHOLD:
        print("[ACTION] Temperature too high. Turning ON air conditioner.")
    elif temp < HEATING_THRESHOLD:
        print("[ACTION] Temperature too low. Turning ON heater.")
    else:
        print("[ACTION] Temperature is optimal. Thermostat remains idle.")

def main():
    temp = get_weather()
    if temp is not None:
        adjust_thermostat(temp)

if __name__ == "__main__":
    main()
