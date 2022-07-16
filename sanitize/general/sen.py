from pathlib import Path
from typing import Any

from sanitize.base import SanitizeBase


class SanitizeSEN(SanitizeBase):
    path_mapping_special = {
        (2017, 2018, "3f.csv"): Path("general/performance/SEN/allCandidates.json"),
        (2019, -1, "3g.csv"): Path("general/performance/SEN/allCandidates.json"),
    }

    key_rename = {
        "Description": "description",
        "Total": "total"
    }

    def process(self, raw_data: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
        data = []
        for row in raw_data:
            del row["No."]
            if "Type" in row:
                del row["Type"]
            data.append(row)

        return data
