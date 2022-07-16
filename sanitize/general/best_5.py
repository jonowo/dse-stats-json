from pathlib import Path

from sanitize.general.general import SanitizeGeneralDaySchoolCandidates


class SanitizeBest5DaySchoolCandidates(SanitizeGeneralDaySchoolCandidates):
    path_mapping = {}
    path_mapping_special = {
        (2019, -1, "3e_2a.csv"): (
            Path("general/grade-point-distribution/4C1X-33222/best-5/daySchoolCandidates.json"),
            Path("general/grade-point-distribution/4C1X-33222/4C1X/daySchoolCandidates.json")
        )
    }

    key_rename = {}
    key_rename_1 = {
        "Description": "description",
        "Day school candidates taking at least five Category A / B subjects (Any five subjects) - Male": "male",
        "Day school candidates taking at least five Category A / B subjects (Any five subjects) - Female": "female",
        "Day school candidates taking at least five Category A / B subjects (Any five subjects) - Total": "total"
    }
    key_rename_2 = {
        "Description": "description",
        "Day school candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Male": "male",
        "Day school candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Female": "female",
        "Day school candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Total": "total"
    }

    def preprocess(self) -> None:
        if self.json_path.parts[-2] == "best-5":
            self.key_rename = self.key_rename_1
        else:
            self.key_rename = self.key_rename_2


class SanitizeBest5AllCandidates(SanitizeBest5DaySchoolCandidates):
    path_mapping_special = {
        (2019, -1, "3e_2b.csv"): (
            Path("general/grade-point-distribution/4C1X-33222/best-5/allCandidates.json"),
            Path("general/grade-point-distribution/4C1X-33222/4C1X/allCandidates.json")
        )
    }

    key_rename_1 = {
        "Description": "description",
        "All candidates taking at least five Category A / B subjects (Any five subjects) - Male": "male",
        "All candidates taking at least five Category A / B subjects (Any five subjects) - Female": "female",
        "All candidates taking at least five Category A / B subjects (Any five subjects) - Total": "total"
    }
    key_rename_2 = {
        "Description": "description",
        "All candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Male": "male",
        "All candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Female": "female",
        "All candidates taking at least five Category A / B subjects (Four core subjects and one elective subject) - Total": "total"
    }
