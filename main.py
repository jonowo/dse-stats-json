import csv
import json
from collections import defaultdict

for year in range(2017, 2022):
    for filename in "ab":
        with open(f"data/{year}/{filename}.csv") as f:
            if f.read(1) != "\ufeff":  # ZERO WIDTH NO-BREAK SPACE
                f.seek(0, 0)
            reader = csv.DictReader(f)
            raw_data = list(reader)

        # Sanitize
        for row in raw_data:
            for key in list(row):
                new_key = key.replace("\n", " ").replace(
                    " -  ", " - ").strip().lower()
                if new_key.endswith("5*"):
                    new_key += "+"
                row[new_key] = row.pop(key)

        data = []
        for row in raw_data:
            if row["type"] == "Number":
                data.append(row)
            elif row["chinese version %"]:
                data[-1]["chinese version %"] = row["chinese version %"]

        subjects = defaultdict(dict)
        for row in data:
            p = (row["subject"], row["subject_2"] or None)
            subjects[p][row["gender"].lower()] = {
                "no_entered": int(row["no. entered"]),
                "no_sat": int(row["no. sat"]),
                "chin_ver": ("-" if row["chinese version %"] == "-"
                             else float(row["chinese version %"])),
                "5**": int(row["performance - 5**"]),
                "5*+": int(row["performance - 5*+"]),
                "5+": int(row["performance - 5+"]),
                "4+": int(row["performance - 4+"]),
                "3+": int(row["performance - 3+"]),
                "2+": int(row["performance - 2+"]),
                "1+": int(row["performance - 1+"]),
                "U": int(row["performance - u"])
            }

        data = [
            {
                "subject": k[0],
                "subject_2": k[1],
                **v
            } for k, v in subjects.items()
        ]

        with open(f"data/{year}/{filename}.json", "w") as f:
            json.dump(data, f, indent=4)
