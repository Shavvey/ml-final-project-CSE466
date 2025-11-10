import json
import re as regex
import os
import csv as csv
from data.dataframe import DataFrame

# directory that contains all the json files
JSON_DATA_DIR_PATH = "json/"
CSV_FILE_PATH = "csv/clinical_info_and_vf_baseline.csv"


@staticmethod
def get_all_image_data():
    # first let's find all the json files in that `json` dir
    json_files: list[str] = []
    # create regular expression we match against
    rexp = regex.compile("^[a-zA-Z0-9_]*.json")
    # walk the directory structure and find files that match regular expression
    for root, _, files in os.walk(JSON_DATA_DIR_PATH):
        for file in files:
            if rexp.match(file):
                full_path = os.path.join(root, file)
                json_files.append(full_path)
    print(len(json_files))
    if len(json_files) == 0:
        raise Exception("Could not find any JSON files")
    # now try and parse the json files
    for file in json_files:
        with open(file, "r") as file:
            data = json.load(file)
            print(data)


@staticmethod
def make_data() -> list[DataFrame]:
    """This helper function should return a training
    and test set that can be used for our resnet classification model"""
    with open(CSV_FILE_PATH, "r") as csv_file:
        # construct csv reader object
        csv_reader = csv.reader(csv_file)
        # throw out the header
        _ = csv_reader.__next__()
        for row in csv_reader:
            # find json file with image data
            json_file_path = JSON_DATA_DIR_PATH + row[5] + ".json"
            with open(json_file_path, "r") as file:
                data = json.load(file)
                print(data)


if __name__ == "__main__":
    make_data()
