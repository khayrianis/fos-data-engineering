# FOS Data Engineer - Weather Data ETL Process

This repository contains a Python project called FOS-Data-Engineer, which aims to apply an Extract, Transform, Load (ETL) process to obtain weather data for cities in Algeria. The ETL process involves retrieving the latitude and longitude of the cities using the 'https://nominatim.openstreetmap.org' API and fetching weather data for the corresponding coordinates using the 'https://api.open-meteo.com' API. The project also includes a cron job configuration file to automate the ETL process to run every 30 minutes.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- pandas
- requests
- folium

## Project Structure

The project is organized as follows:

- `cities.json`: This file contains an array of city names in Algeria for which you want to extract weather data.
- `extract.py`: This script utilizes the two APIs mentioned above to extract weather data for the specified cities. The extracted data is saved in a JSON file named 'raw*data*{unix_timestamp}.json', where the 'unix_timestamp' represents the time of the extracted data.
- `transform.py`: This script processes the raw weather data files (JSON format) and transforms them into a CSV file named 'transformed_data.csv'.
- `load.py`: This script loads the transformed geolocated data from the CSV file and utilizes the folium library to create a map displaying cities and their current temperature.
- `etl.py`: This is the main file that orchestrates the entire ETL process. It sequentially executes the extract, transform, and load steps.
- `cronfile`: This file contains the cron job configuration to schedule the execution of `etl.py` every 30 minutes.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/FOS-Data-Engineer.git
```

2. Install the required dependencies.

```bash
pip install pandas requests folium
```

3. Ensure that the `cities.json` file contains the names of the cities in Algeria for which you want to extract weather data.

4. Run the ETL process manually by executing the following command:

```bash
python etl.py
```

This will trigger the extraction of weather data for the specified cities, followed by the transformation into a CSV file and the creation of a map with the cities' current temperature.

5. If you wish to automate the ETL process to run every 30 minutes, configure the cron job using the `cronfile` provided. This file specifies the frequency and command to execute `etl.py`. Update the paths in the `cronfile` to match your local environment, and then add the cron job using the following command:

```bash
crontab cronfile
```

The cron job will now execute `etl.py` every 30 minutes, ensuring that the weather data remains up to date.

## Conclusion

The FOS-Data-Engineer project provides a simple yet effective ETL process for retrieving weather data for cities in Algeria. By utilizing the provided scripts, you can easily extract, transform, and load the data, as well as automate the process using a cron job. Feel free to customize the project according to your requirements and expand it further if needed.

For any questions or issues, please open an issue on the [repository](https://github.com/khayrianis/fos-data-engineering/issues).
