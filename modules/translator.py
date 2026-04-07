import csv


def is_number(token):
    try:
        float(token)
        return True
    except Exception:
        return False


def tokenize_line(line):
    return [t.strip() for t in line.split(",")]


def parse_tokens(tokens, cycle_id):
    rows = []
    i = 0

    while i < len(tokens) - 1:
        label = tokens[i]

        if label == "":
            i += 1
            continue

        values = [tokens[i + 1]]
        i += 2

        while i < len(tokens):
            token = tokens[i]

            if token and not is_number(token):
                break

            values.append(token)
            i += 1

        for axis, value in enumerate(values):
            rows.append({
                "Cycle": cycle_id,
                "Feature": label,
                "ValueNumber": axis + 1,
                "Value": value
            })

    return rows


def run_translation(input_file, output_file):
    all_rows = []
    cycle = 0

    with open(input_file, "r") as f:
        for line in f:
            tokens = tokenize_line(line)

            if not tokens:
                continue

            parsed = parse_tokens(tokens, cycle)

            if not parsed:
                continue

            all_rows.extend(parsed)
            cycle += 1

    if not all_rows:
        raise RuntimeError("No data parsed from input file.")

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["Cycle", "Feature", "ValueNumber", "Value"]
        )
        writer.writeheader()
        writer.writerows(all_rows)
