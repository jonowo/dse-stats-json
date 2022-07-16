from collections import defaultdict
from pathlib import Path
from typing import Any

from sanitize.base import SanitizeBase
from sanitize.utils import int_if_not_none


class SanitizeCategoryCSubjects(SanitizeBase):
    path_mapping = {
        "5e.csv": Path("subjects/c/daySchoolCandidates.json"),
        "5f.csv": Path("subjects/c/allCandidates.json")
    }

    key_rename = {
        "Subject": "subject",
        "No. Entered": "noEntered",
        "No. entered": "noEntered",
        "No. Sat": "noSat",
        "No. sat": "noSat",
        "Performance - a": "a",
        "Performance - b+": "b+",
        "Performance - c+": "c+",
        "Performance - d+": "d+",
        "Performance - e+": "e+",
        "Performance - U": "U",
    }

    def process(self, raw_data: list[dict[str, Any]]) -> Any:
        data = [row for row in raw_data if row["Type"] == "Number"]

        subjects = defaultdict(dict)
        for row in data:
            p = row["subject"]
            subjects[p][row["gender"]] = {
                "noEntered": int(row["noEntered"]),
                "noSat": int(row["noSat"]),
                "a": int_if_not_none(row["a"]),
                "b+": int_if_not_none(row["b+"]),
                "c+": int_if_not_none(row["c+"]),
                "d+": int_if_not_none(row["d+"]),
                "e+": int_if_not_none(row["e+"]),
                "U": int_if_not_none(row["U"])
            }

        data = [{"subject": k, **v} for k, v in subjects.items()]
        return data
