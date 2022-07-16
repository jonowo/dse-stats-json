from collections import defaultdict
from pathlib import Path
from typing import Any

from sanitize.base import SanitizeBase
from sanitize.utils import int_if_not_none


class SanitizeCategoryASubjects(SanitizeBase):
    path_mapping = {
        "5a.csv": Path("subjects/a/daySchoolCandidates.json"),
        "5b.csv": Path("subjects/a/allCandidates.json")
    }

    key_rename = {
        "Subject": "subject",
        "Subject_2": "subcategory",
        "No. Entered": "noEntered",
        "No. entered": "noEntered",
        "No. Sat": "noSat",
        "No. sat": "noSat",
        "Chinese Version %": "chineseVersion",
        "Chinese version %": "chineseVersion",
        "Performance - 5**": "5**",
        "Performance - 5*+": "5*+",
        "Performance - 5*": "5*+",
        "Performance - 5+": "5+",
        "Performance - 4+": "4+",
        "Performance - 3+": "3+",
        "Performance - 2+": "2+",
        "Performance - 1+": "1+",
        "Performance - U": "U"
    }

    def process(self, raw_data: list[dict[str, Any]]) -> Any:
        data = []
        for row in raw_data:
            if row["Type"] == "Number":
                data.append(row)
            elif data and data[-1]["chineseVersion"] == "":
                data[-1]["chineseVersion"] = row["chineseVersion"]

        subjects = defaultdict(dict)
        for row in data:
            p = (
                row["subject"].rstrip("#"),
                row["subcategory"] or None
            )
            subjects[p][row["gender"]] = {
                "noEntered": int(row["noEntered"]),
                "noSat": int(row["noSat"]),
                "chineseVersion": (None if row["chineseVersion"] is None
                                   else float(row["chineseVersion"])),
                "5**": int_if_not_none(row["5**"]),
                "5*+": int_if_not_none(row["5*+"]),
                "5+": int_if_not_none(row["5+"]),
                "4+": int_if_not_none(row["4+"]),
                "3+": int_if_not_none(row["3+"]),
                "2+": int_if_not_none(row["2+"]),
                "1+": int_if_not_none(row["1+"]),
                "U": int_if_not_none(row["U"])
            }

        data = [
            {
                "subject": k[0],
                "subcategory": k[1],
                **v
            } for k, v in subjects.items()
        ]
        return data
