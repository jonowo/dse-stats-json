from collections import defaultdict
from pathlib import Path
from typing import Any

from sanitize.base import SanitizeBase
from sanitize.utils import int_if_not_none


class SanitizeCategoryBSubjects(SanitizeBase):
    path_mapping_special = {
        (2017, 2017, "5c.csv"): Path("subjects/b/daySchoolCandidates.json"),
        (2017, 2017, "5d.csv"): Path("subjects/b/allCandidates.json"),
        (2018, -1, "5c_1.csv"): Path("subjects/b/daySchoolCandidates.json"),
        (2018, -1, "5c_2.csv"): Path("subjects/b-chinese/daySchoolCandidates.json"),
        (2018, -1, "5d_1.csv"): Path("subjects/b/allCandidates.json"),
        (2018, -1, "5d_2.csv"): Path("subjects/b-chinese/allCandidates.json")
    }

    key_rename = {
        "Subject": "subject",
        "Subject_2": "subcategory",
        "No. Entered": "noEntered",
        "No. entered": "noEntered",
        "No. of candidates fulfilling attendance requirement": "noFulfillingAttendanceRequirement"
    }

    def process(self, raw_data: list[dict[str, Any]]) -> Any:
        data = [row for row in raw_data if row["Type"] == "Number"]

        subjects = defaultdict(dict)
        for row in data:
            if row["subject"] == "Applied Learning Chinese (for non-Chinese speaking students)":
                subcategory = row["subcategory"] or "All"
            else:
                subcategory = row["subcategory"] or None
            p = (row["subject"], subcategory)

            if self.csv_filename.endswith("1.csv"):
                gender_data = {
                    "noEntered": int(row["noEntered"]),
                    "noFulfillingAttendanceRequirement": int(row["noFulfillingAttendanceRequirement"]),
                    "Attained with Distinction (II)": int_if_not_none(row["Attained with Distinction (II)"]),
                    "Attained with Distinction (I) or above": int_if_not_none(row["Attained with Distinction (I) or above"]),
                    "Attained or above": int_if_not_none(row["Attained or above"]),
                    "Unattained": int_if_not_none(row["Unattained"])
                }
            else:
                gender_data = {
                    "noEntered": int(row["noEntered"]),
                    "noFulfillingAttendanceRequirement": int(row["noFulfillingAttendanceRequirement"]),
                    "Attained with Distinction": int_if_not_none(row["Attained with Distinction"]),
                    "Attained or above": int_if_not_none(row["Attained or above"]),
                    "Unattained": int_if_not_none(row["Unattained"])
                }

            subjects[p][row["gender"]] = gender_data

        data = [
            {
                "subject": k[0],
                "subcategory": k[1],
                **v
            } for k, v in subjects.items()
        ]
        return data
