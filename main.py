import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from os import walk

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)

data_path = "C:/Datasets/AirbnbMunich/"


def save_descriptions(description_object):
    for key in description_object:
        description_object[key].describe(include="all").to_html("./out/descriptions/%s.html" % key)


def load_csv_from_dir(directory):
    ret = {}
    for root, dirs, files in walk(directory):
        for file in files:
            if file.endswith(".csv"):
                key = file.replace(".csv", "")
                df = pd.read_csv(root + file, low_memory=False)
                ret[key] = df
    return ret


def listings_per_host(data_frame):
    amount_listings = data_frame["host_id"].count()
    print("amount of listing entries: %d" % amount_listings)

    amount_hosts = data_frame["host_id"].drop_duplicates().count()
    print("Without duplicates: %d" % amount_hosts)

    l_per_host = amount_listings / amount_hosts
    print("Average listings per host: %10.6f" % l_per_host)

    multiple_listing_hosts = data_frame[data_frame["host_id"].duplicated()]
    print("Amount of hosts with multiple listings: %d" % multiple_listing_hosts["host_id"].count())
    print("Amount of hosts with multiple listings: %d (dropped)" % multiple_listing_hosts[
        "host_id"].drop_duplicates().count())
    listings_per_host_with_multiple = multiple_listing_hosts["host_id"].count() / multiple_listing_hosts[
        "host_id"].drop_duplicates().count()
    print("Listings per host with multiple listings: %10.6f" % listings_per_host_with_multiple)

    most_listings_host_id = multiple_listing_hosts["host_id"].value_counts().argmax()
    print("host with most listings id: %d " % most_listings_host_id)

    mlh_listings = data_frame[data_frame["host_id"] == most_listings_host_id]
    print(mlh_listings)


data = load_csv_from_dir(data_path)
listings_s = data["listings_smal"]
# save_descriptions(data)

listings_per_host(listings_s)
