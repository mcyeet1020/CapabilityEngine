import csv
from collections import defaultdict


def export_wide(input_csv, output_csv):
    with open(input_csv, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    columns = set()
    data = defaultdict(dict)

    for row in rows:
        cycle = row["Cycle"]
        feature = row["Feature"]
        valuenum = row["ValueNumber"]
        value = row["Value"]

        if cycle == "":
            continue

        col_name = f"{feature}_{valuenum}"
        columns.add(col_name)

        data[cycle][col_name] = value

    columns = sorted(columns)

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Cycle"] + columns)

        for cycle in sorted(data.keys(), key=int):
            row = [cycle]
            for col in columns:
                row.append(data[cycle].get(col, "N/A"))

            writer.writerow(row)
