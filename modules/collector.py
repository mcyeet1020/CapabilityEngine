import csv


def collect_and_clean(input_csv, output_csv):
    with open(input_csv, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    cleaned = []
    last_cycle = None

    for row in rows:
        cycle = row["Cycle"]
        feature = row["Feature"]
        valuenum = row["ValueNumber"]
        value = row["Value"]

        if feature == "" and value == "":
            continue

        if value == "":
            if valuenum == "1":
                row["Value"] = "N/A"
            else:
                continue

        if last_cycle is not None and cycle != last_cycle:
            cleaned.append({
                "Cycle": "",
                "Feature": "",
                "ValueNumber": "",
                "Value": ""
            })

        cleaned.append(row)
        last_cycle = cycle

    with open(output_csv, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Cycle", "Feature", "ValueNumber", "Value"]
        )
        writer.writeheader()
        writer.writerows(cleaned)
