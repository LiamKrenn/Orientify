import requests
import json
import random

DB_URL = "backend.orientify.krenn.tech"

# Sample data
data = {
  "angle": 0
}

# URL of the API endpoint
url = f"http://{DB_URL}/orientation"

# Function to send data to the API
def send_data(data):
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, data=json.dumps(data), headers=headers)
  if response.status_code != 201:
    print(f"Failed to send data. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
  # You can modify the data here to send different angles
  for angle in range(0, 361, 10):  # Example: sending data for every 10 degrees
    data["angle"] = angle
    for i in range(10 + random.randint(-5, 5)):  # Example: sending data 10 times with a random offset
      send_data(data)