import csv
from dataclasses import asdict


def generate_output(data, field_names):
    fieldnames = field_names
    filename = "data.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows([{**asdict(row)} for row in data])
    return filename
