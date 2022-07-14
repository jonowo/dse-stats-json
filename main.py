import csv
import json
import os
import re
from collections import defaultdict


def remove_duplicate_space(s):
    return re.sub(r"\s+", " ", s.strip())


for year in os.listdir("raw"):
    os.makedirs(f"data/{year}", exist_ok=True)

    for filename in "ab":
        with open(f"raw/{year}/{filename}.csv") as f:
            if f.read(1) != "\ufeff":  # ZERO WIDTH NO-BREAK SPACE
                f.seek(0, 0)
            reader = csv.DictReader(f)
            raw_data = list(reader)

        # Sanitize
        for row in raw_data:
            for key in list(row):
                new_key = remove_duplicate_space(key).lower()
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
            p = (
                remove_duplicate_space(row["subject"]).rstrip("#"),
                remove_duplicate_space(row["subject_2"]) or None
            )
            subjects[p][row["gender"].lower()] = {
                "noEntered": int(row["no. entered"]),
                "noSat": int(row["no. sat"]),
                "chineseVersion": (None if row["chinese version %"] == "-"
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
                "subcategory": k[1],
                **v
            } for k, v in subjects.items()
        ]

        with open(f"data/{year}/{filename}.json", "w") as f:
            json.dump(data, f, indent=4)
