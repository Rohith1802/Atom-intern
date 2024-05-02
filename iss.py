import requests
import json

def get_iss_location():
 
  url = "http://api.open-notify.org/iss-now.json"
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)
    return {
      "latitude": float(data["iss_position"]["latitude"]),
      "longitude": float(data["iss_position"]["longitude"])
    }
  except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
    return None

def res(location):
  if location is None:
    return "Error"
  return f"Lat: {location['latitude']:.2f} and Long: {location['longitude']:.2f}"

if __name__ == "__main__":
  iss_location = get_iss_location()
  print(res(iss_location))
