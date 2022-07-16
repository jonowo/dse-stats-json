from pathlib import Path

from sanitize.general.general import SanitizeGeneralDaySchoolCandidates


class SanitizeBest6DaySchoolCandidates(SanitizeGeneralDaySchoolCandidates):
    path_mapping = {}
    path_mapping_special = {
        (2019, -1, "3f_2a.csv"): (
            Path("general/grade-point-distribution/4C2X-332233/best-6/daySchoolCandidates.json"),
            Path("general/grade-point-distribution/4C2X-332233/4C2X/daySchoolCandidates.json")
        )
    }

    key_rename = {}
    key_rename_1 = {
        "Description": "description",
        "Day school candidates taking at least six Category A / B subjects (Any six subjects) - Male": "male",
        "Day school candidates taking at least six Category A / B subjects (Any six subjects) - Female": "female",
        "Day school candidates taking at least six Category A / B subjects (Any six subjects) - Total": "total"
    }
    key_rename_2 = {
        "Description": "description",
        "Day school candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Male": "male",
        "Day school candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Female": "female",
        "Day school candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Total": "total"
    }

    def preprocess(self) -> None:
        if self.json_path.parts[-2] == "best-6":
            self.key_rename = self.key_rename_1
        else:
            self.key_rename = self.key_rename_2


class SanitizeBest6AllCandidates(SanitizeBest6DaySchoolCandidates):
    path_mapping_special = {
        (2019, -1, "3f_2b.csv"): (
            Path("general/grade-point-distribution/4C2X-332233/best-6/allCandidates.json"),
            Path("general/grade-point-distribution/4C2X-332233/4C2X/allCandidates.json")
        )
    }

    key_rename_1 = {
        "Description": "description",
        "All candidates taking at least six Category A / B subjects (Any six subjects) - Male": "male",
        "All candidates taking at least six Category A / B subjects (Any six subjects) - Female": "female",
        "All candidates taking at least six Category A / B subjects (Any six subjects) - Total": "total"
    }
    key_rename_2 = {
        "Description": "description",
        "All candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Male": "male",
        "All candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Female": "female",
        "All candidates taking at least six Category A / B subjects (Four core subjects and two elective subjects) - Total": "total"
    }
