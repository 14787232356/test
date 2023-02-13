import requests
import datetime

url = "http://www.celestrak.com/NORAD/elements/active.txt"

response = requests.get(url)

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"active_{current_time}.txt"

with open(filename, "w") as f:
    f.write(response.text)

print(f"File saved to {filename}")