from pathlib import Path
from typing import Any

from sanitize.general.general import SanitizeGeneralDaySchoolCandidates


class SanitizeLevelDistribution(SanitizeGeneralDaySchoolCandidates):
    path_mapping = {}
    path_mapping_special = {
        (2017, 2018, "3g.csv"): Path("general/level-distribution/lang/daySchoolCandidates.json"),
        (2017, 2018, "3h.csv"): Path("general/level-distribution/lang/allCandidates.json"),
        (2019, -1, "3h.csv"): Path("general/level-distribution/lang/daySchoolCandidates.json"),
        (2019, -1, "3i.csv"): Path("general/level-distribution/lang/allCandidates.json"),
        (2017, 2018, "3i.csv"): Path("general/level-distribution/math/daySchoolCandidates.json"),
        (2017, 2018, "3j.csv"): Path("general/level-distribution/math/allCandidates.json"),
        (2019, -1, "3j.csv"): Path("general/level-distribution/math/daySchoolCandidates.json"),
        (2019, -1, "3k.csv"): Path("general/level-distribution/math/allCandidates.json")
    }

    key_rename = {}

    def process(self, raw_data: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
        data = {}
        for row in raw_data:
            if row["Type"] == "Number":
                for key in list(row):
                    value = row.pop(key)
                    if key.startswith("Attainment"):
                        if "-" in key:
                            row[key.split(" ")[-1]] = int(value or 0)
                        else:
                            level = value
                    elif key == "Total":
                        row["total"] = int(value or 0)

                if level == "Total":
                    level = "total"
                data[level] = row

        return data
