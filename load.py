import pandas as pd
import folium
import logging

# Configure logging
logging.basicConfig(
    filename="logfile.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("We are in loading step.")


def main():
    data = pd.read_csv("transformed_data.csv")
    map = folium.Map(location=[28.0339, 1.6596], zoom_start=5)
    for index, row in data.iterrows():
        city = row["city"]
        temperature = row["temperature"]
        popup_text = f"{city}: {temperature} °C"
        marker = folium.Marker(
            location=[row["latitude"], row["longitude"]], popup=popup_text
        )
        marker.add_to(map)
    logging.info("Save the map.")
    map.save("map.html")


if __name__ == "__main__":
    main()
