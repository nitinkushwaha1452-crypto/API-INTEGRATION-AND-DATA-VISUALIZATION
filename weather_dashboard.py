import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "9b177fa58942a7fe34c35723d65d106a"
CITY = "Nagpur"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# -------- ERROR HANDLING --------
if response.status_code != 200:
    print("Error fetching data:")
    print(data)
    exit()

# -------- DATA EXTRACTION --------
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

weather_data = {
    "Temperature (°C)": temperature,
    "Feels Like (°C)": feels_like,
    "Humidity (%)": humidity,
    "Pressure (hPa)": pressure
}

# -------- VISUALIZATION --------
sns.set()
plt.figure(figsize=(10, 6))
sns.barplot(x=list(weather_data.keys()), y=list(weather_data.values()))
plt.title(f"Weather Dashboard - {CITY}")
plt.xlabel("Parameters")
plt.ylabel("Values")
plt.tight_layout()
plt.show()
