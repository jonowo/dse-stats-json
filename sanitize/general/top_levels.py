from pathlib import Path
from typing import Any

from sanitize.general.general import SanitizeGeneralDaySchoolCandidates


class SanitizeTopLevels(SanitizeGeneralDaySchoolCandidates):
    path_mapping = {}
    path_mapping_special = {
        (2017, 2018, "3k.csv"): (
            Path("general/performance/top-levels/a/daySchoolCandidates.json"),
            Path("general/performance/top-levels/a-b-c/daySchoolCandidates.json")
        ),
        (2017, 2018, "3l.csv"): (
            Path("general/performance/top-levels/a/allCandidates.json"),
            Path("general/performance/top-levels/a-b-c/allCandidates.json")
        ),
        (2019, -1, "3l.csv"): (
            Path("general/performance/top-levels/a/daySchoolCandidates.json"),
            Path("general/performance/top-levels/a-b-c/daySchoolCandidates.json")
        ),
        (2019, -1, "3m.csv"): (
            Path("general/performance/top-levels/a/allCandidates.json"),
            Path("general/performance/top-levels/a-b-c/allCandidates.json")
        )
    }

    key_rename = {}
    key_rename_1 = {
        "Total no. of subjects at top levels / grades": "description",
        "Candidates with the corresponding results in Category A subjects - No. of Male": "male",
        "Candidates with the corresponding results in Category A subjects - No of Male": "male",
        "Candidates with the corresponding results in Category A subjects - No. of Female": "female",
        "Candidates with the corresponding results in Category A subjects - No of Female": "female",
        "Candidates with the corresponding results in Category A subjects - Total No.": "total",
        "Candidates with the corresponding results in Category A subjects - Total No": "total",
        "Candidates with the corresponding results in Category A subjects - Total no": "total"
    }
    key_rename_2 = {
        "Total no. of subjects at top levels / grades": "description",
        "Candidates with the corresponding results in Category A/B/C subjects - No. of Male": "male",
        "Candidates with the corresponding results in Category A/B/C subjects - No of Male": "male",
        "Candidates with the corresponding results in Category A/B/C subjects - No. of Female": "female",
        "Candidates with the corresponding results in Category A/B/C subjects - No of Female": "female",
        "Candidates with the corresponding results in Category A/B/C subjects - Total No.": "total",
        "Candidates with the corresponding results in Category A/B/C subjects - Total no": "total",
        "Candidates with the corresponding results in Category A/B/C subjects - Total No": "total"
    }

    def preprocess(self) -> None:
        if self.json_path.parts[-2] == "a":
            self.key_rename = self.key_rename_1
        else:
            self.key_rename = self.key_rename_2


    def process(self, raw_data: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
        data = []
        for row in raw_data:
            data.append({
                "description": row["description"],
                "male": int(row["male"]),
                "female": int(row["female"]),
                "total": int(row["total"])
            })

        return data
