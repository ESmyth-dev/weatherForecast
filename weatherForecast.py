import requests
import json
import argparse

def api_query(city):
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}")
    if(response):
        json_data = json.loads(response.text)
        temp_c = json_data['current']['temp_c']
        print(f"Today it is {temp_c}°C in {city}.")
    else:
        print("Sorry that is not a valid city, please try again later.")


parser = argparse.ArgumentParser()
parser.add_argument("city")
args = parser.parse_args()
city = args.city
city = city.strip()    
city = city.capitalize()

with open('secrets.json') as secrets_file:
    secrets_data = json.load(secrets_file)
api_key = secrets_data['api_key']

        
api_query(city)




