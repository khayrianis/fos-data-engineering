import json
import time
import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("We are in exctracting step.")


def get_list_of_cities():
    logging.info("Excuting get_list_of_cities().")
    with open("cities.json", "r") as file:
        return json.load(file)


def get_lat_lon(city):
    logging.info(f"Get the latitude and longtitude for {city}")
    url = f"https://nominatim.openstreetmap.org/search?city={city}&country=Algeria&format=json"

    response = requests.get(
        url=url,
    )
    if response.status_code == 200:
        return response.json()[0].get("lat"), response.json()[0].get("lon")
    else:
        print("Failed to retrieve weather data.")
    pass


def get_current_weather(lat, lon):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m",
    )
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve weather data.")


def get_weather_all_cities(cities):
    data = dict()
    for city in cities:
        lat, lon = get_lat_lon(city)
        res = get_current_weather(lat, lon)
        data[city] = res
    return data


def save_output_data(data_):
    logging.info(f"Save output data")
    unix_timestamp = int(time.time())
    output_filename = f"raw_data_{unix_timestamp}.json"
    with open(output_filename, "w") as f:
        json.dump(data_, f)


def main():
    cities = get_list_of_cities()
    # print(cities)
    weather_data = get_weather_all_cities(cities)
    # print(weather_data)
    save_output_data(weather_data)


if __name__ == "__main__":
    for i in range(3):
        main()
