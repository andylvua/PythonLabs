import os
import re
import zipfile

from datetime import datetime

import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import seaborn as sns


def read_zip_file(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall("resources/")

    with open(file_path.strip(".zip")) as file:
        lines = [line for line in file]
        os.remove(file_path.strip(".zip"))

    return lines


def statistics_of_requests_in_datetime_range(file_path, start_datetime, end_datetime):
    lines = read_zip_file(file_path)

    start = datetime.strptime(start_datetime, "%d/%b/%Y:%H:%M:%S")
    end = datetime.strptime(end_datetime, "%d/%b/%Y:%H:%M:%S")

    info = dict()

    for line in lines:
        datetime_match = (re.search("\[(.*?)]", line)).group(0)
        time = datetime_match.strip("[]").split("-")[0].strip()
        time_formatted = datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')

        status_code_match = (re.search("\s\d{3}\s", line)).group(0).strip()

        if start <= time_formatted <= end:
            info[status_code_match] = info.get(status_code_match, 0) + 1

    print_statistics(file_path, info, start_datetime, end_datetime)
    show_statistics_plot(file_path, info, start_datetime, end_datetime)


def print_statistics(file_path, info, start_datetime, end_datetime):
    successful_requests_quantity = int()
    unsuccessful_requests_quantity = int()

    all_requests = dict()

    for key, value in info.items():
        if key.startswith("2"):
            successful_requests_quantity += value
            all_requests.setdefault("successful", {})[key] = all_requests.get("successful", {}).get(key, 0) + value
        else:
            unsuccessful_requests_quantity += value
            all_requests.setdefault("unsuccessful", {})[key] = all_requests.get("unsuccessful", {}).get(key, 0) + value

    all_requests["successful"] = dict(sorted(
        all_requests["successful"].items(), key=lambda item: item[1], reverse=True))
    all_requests["unsuccessful"] = dict(sorted(
        all_requests["unsuccessful"].items(), key=lambda item: item[1], reverse=True))

    file_name = file_path.split('/')[-1].strip(".zip")

    successful_requests_codes = str()
    unsuccessful_requests_codes = str()

    for key, value in all_requests["successful"].items():
        successful_requests_codes += f"code {key} in quantity of {value}\n"

    for key, value in all_requests["unsuccessful"].items():
        unsuccessful_requests_codes += f"code {key} in quantity of {value}\n"

    output = f"File: {file_name}\n" \
             f"In period from {start_datetime} to {end_datetime} there were\n" \
             f"{successful_requests_quantity} successful requests, where:\n" \
             + successful_requests_codes \
             + f"and {unsuccessful_requests_quantity} unsuccessful requests, where:\n" \
             + unsuccessful_requests_codes

    print(output)


def show_statistics_plot(file_path, info, start_datetime, end_datetime):
    df = pd.DataFrame(info.items(), columns=['Status code', 'Quantity'])
    df.sort_values(by='Quantity', ignore_index=True, ascending=False, inplace=True)

    plot = plt.figure(figsize=(15, 10))

    palette = ['#32CD32' if int(val) in range(200, 300) else '#E50000' for val in (df['Status code'].tolist())]

    sns.barplot(
        x="Status code",
        y="Quantity",
        data=df,
        estimator=sum,
        palette=palette
    )

    file_name = file_path.split('/')[-1].strip(".zip")

    plt.gca().set_title(file_name, fontsize=20, fontweight='bold', pad=20)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.xticks(fontsize=14)
    plt.xlabel("Status code", fontsize=14, fontweight='bold', labelpad=20)
    plt.yticks(fontsize=14)
    plt.ylabel("Quantity", fontsize=14, fontweight='bold', labelpad=20)

    plt.show()
