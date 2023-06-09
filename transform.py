import glob
import json
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("We are in transforming step.")


def get_all_filenames():
    # this function should return a list of filenames
    # you should look at glob library
    # Example: it should return ["raw_data_1686027160.json", "raw_data_1686027165.json", "raw_data_1686027170.json"]
    logging.info("Get all filenames.")
    return glob.glob("raw_data_*.json")


def transform_one_file(filename):
    # this function should return a list of dictionaries
    # each dictionnary should look like that: { "city": city, "latitude": latitude, "longitude": longitude , "temperature": tempature, "time": time}
    logging.info(f"Transform {filename}.")
    with open(filename, "r") as file:
        data: dict = json.load(file)
    transformed_data = [
        {
            "city": k,
            "latitude": v.get("latitude"),
            "longitude": v.get("longitude"),
            "temperature": v.get("current_weather").get("temperature"),
            "time": v.get("current_weather").get("time"),
        }
        for k, v in data.items()
    ]
    return transformed_data


def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
    df = pd.DataFrame(output)
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M")
    return df


def drop_duplicates(df_: pd.DataFrame):
    return df_.drop_duplicates()


def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    # print(df.head())
    df = drop_duplicates(df)
    logging.info("Save to csv.")
    df.to_csv("transformed_data.csv", index=False)


if __name__ == "__main__":
    main()
