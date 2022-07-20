import re
from pathlib import Path
from typing import Any

from sanitize.base import SanitizeBase


class SanitizeGeneralDaySchoolCandidates(SanitizeBase):
    path_mapping = {
        "3a.csv": Path("general/performance/level-2/daySchoolCandidates.json"),
        "3b.csv": Path("general/performance/best-5/daySchoolCandidates.json"),
        "3c_2.csv": Path("general/grade-point-distribution/CE3X-22222/CE3X/daySchoolCandidates.json"),
        "3d.csv": Path("general/performance/university/daySchoolCandidates.json")
    }
    path_mapping_special = {
        (2017, 2018, "3e.csv"): Path("general/grade-point-distribution/4C-3322/best-5/daySchoolCandidates.json"),
        (2019, -1, "3e_1.csv"): Path("general/grade-point-distribution/4C-3322/best-5/daySchoolCandidates.json"),
        (2019, -1, "3f_1.csv"): Path("general/grade-point-distribution/4C-3322/best-6/daySchoolCandidates.json")
    }

    key_rename = {
        "Description": "description",
        "Descroption": "description",
        "Day school candidates taking at least five Category A / B subjects - Male": "male",
        "Day school candidates taking at least five Category A / B subjects - Female": "female",
        "Day school candidates taking at least five Category A / B subjects - Total": "total",
        "Day school candidates - Male": "male",
        "Day school candidates - Female": "female",
        "Day school candidates - Total": "total",
        "Day school candidates taking at least six Category A / B subjects - Male": "male",
        "Day school candidates taking at least six Category A / B subjects - Female": "female",
        "Day school candidates taking at least six Category A / B subjects - Total": "total"
    }

    def process(self, raw_data: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
        data = []
        for row in raw_data:
            if row["Type"] == "Number":
                if row["description"].lower() == "no of people":
                    row["description"] = "No. of candidates"
                elif row["description"].startswith("Total grade points"):
                    match = re.match(r"^\D+(\d+)\D+(\d+)$", row["description"])
                    row["description"] = f"{match[1]}-{match[2]}"

                data.append({
                    "description": row["description"],
                    "male": int(row["male"]),
                    "female": int(row["female"]),
                    "total": int(row["total"])
                })

        return data


class SanitizeGeneralAllCandidates(SanitizeGeneralDaySchoolCandidates):
    path_mapping = {
        "3a.csv": Path("general/performance/level-2/allCandidates.json"),
        "3b.csv": Path("general/performance/best-5/allCandidates.json"),
        "3c_2.csv": Path("general/grade-point-distribution/CE3X-22222/CE3X/allCandidates.json"),
        "3d.csv": Path("general/performance/university/allCandidates.json")
    }
    path_mapping_special = {
        (2017, 2018, "3e.csv"): Path("general/grade-point-distribution/4C-3322/best-5/allCandidates.json"),
        (2019, -1, "3e_1.csv"): Path("general/grade-point-distribution/4C-3322/best-5/allCandidates.json"),
        (2019, -1, "3f_1.csv"): Path("general/grade-point-distribution/4C-3322/best-6/allCandidates.json")
    }

    key_rename = {
        "Description": "description",
        "Descroption": "description",
        "All candidates taking at least five Category A / B subjects - Male": "male",
        "All candidates taking at least five Category A / B subjects - Female": "female",
        "All candidates taking at least five Category A / B subjects - Famale": "female",
        "All candidates taking at least five Category A / B subjects - Total": "total",
        "All candidates - Male": "male",
        "All candidates - Female": "female",
        "All candidates - Total": "total",
        "All candidates taking at least six Category A / B subjects - Male": "male",
        "All candidates taking at least six Category A / B subjects - Female": "female",
        "All candidates taking at least six Category A / B subjects - Total": "total"
    }
