"""
Day 49 Milestone Project: Live Weather Forecast CLI App ⛅
----------------------------------------------------------
Combine HTTP network requests, API headers, and dynamic parsing by engineering 
a command-line Live Weather Forecast program.

Task Requirements:
1. Use the 'requests' library to call a public weather API.
   - Recommended: OpenWeatherMap API (requires free key) or wttr.in (no key needed!).
   - In this template, we'll write a query to: https://wttr.in/YOUR_CITY?format=j1
2. Ask the user for their target city.
3. Call the API, parse the JSON payload, and print:
   - Location Name
   - Current Temperature (°C / °F)
   - Weather condition description (e.g., Sunny, Rainy)
   - Humidity percentage
4. Implement exception guards for ConnectionError and HTTPError.
"""

import requests

def get_weather(city):
    # We will use the free open-source wttr.in weather API.
    # Wttr.in doesn't require API keys, which is perfect for student practice!
    url = f"https://wttr.in/{city}?format=j1"
    
    print(f"\nFetching weather for {city.capitalize()}...")
    
    try:
        # TODO: Trigger requests.get() on url. Use timeout=10.
        # TODO: Check response status codes using raise_for_status().
        # TODO: Parse response.json() and extract current temperature and conditions.
        # Hint: Wttr.in JSON has a structure like: data['current_condition'][0]
        pass
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: Could not retrieve weather details. ({e})")

def main():
    print("=== Welcome to the Live Weather CLI ===")
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("Invalid input city!")

if __name__ == "__main__":
    main()
