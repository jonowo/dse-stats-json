import csv
import json
import logging
import re
from pathlib import Path
from typing import Any, Iterable, Union

from sanitize.utils import get_years, remove_duplicate_space

logger = logging.getLogger(__name__)


class SanitizeBase:
    path_mapping: dict[str, Union[Path, Iterable[Path]]] = {}
    path_mapping_special: dict[tuple[int, int, str], Union[Path, Iterable[Path]]] = {}
    key_rename: dict[str, str] = {}

    def __init__(self):
        for year in get_years():
            for csv_path, json_paths in self.path_mapping.items():
                if isinstance(json_paths, Path):
                    json_paths = [json_paths]
                for json_path in json_paths:
                    full_csv_path = Path("raw") / year / csv_path
                    full_json_path = Path("data") / year / json_path
                    self.prepare(year, full_csv_path, full_json_path)

        for (*r, csv_path), json_paths in self.path_mapping_special.items():
            if r[0] == -1:
                r[0] = int(get_years()[0])
            if r[1] == -1:
                r[1] = int(get_years()[-1])

            if isinstance(json_paths, Path):
                json_paths = [json_paths]
            for year in map(str, range(r[0], r[1] + 1)):
                for json_path in json_paths:
                    full_csv_path = Path("raw") / year / csv_path
                    full_json_path = Path("data") / year / json_path
                    self.prepare(year, full_csv_path, full_json_path)

    def prepare(self, year: str, full_csv_path: Path, full_json_path: Path) -> None:
        logger.info("Generating %s", full_json_path)

        self.year = int(year)
        self.csv_filename = full_csv_path.name
        self.json_path = full_json_path
        self.preprocess()

        with full_csv_path.open(encoding="utf-8") as f:
            if f.read(1) != "\ufeff":  # ZERO WIDTH NO-BREAK SPACE
                f.seek(0, 0)
            reader = csv.DictReader(f)
            raw_data = list(reader)

        # Common sanitization
        for row in raw_data:
            for key in list(row):
                new_key = key.replace(" -", " - ")
                new_key = re.sub(r"\s*\#\s*", "", new_key)
                new_key = remove_duplicate_space(new_key)
                if new_key == "Gender":
                    row["gender"] = row.pop(key).lower()
                    continue

                new_key = self.key_rename.get(new_key, new_key)
                new_value = remove_duplicate_space(row.pop(key))
                new_value = re.sub(r"\s*\#\s*", "", new_value)
                if (match := re.match(r"(\d+) (\d+)", new_value)):
                    new_value = "".join(match.group(1, 2))

                if new_value == "-":
                    new_value = None

                row[new_key] = new_value
        data = self.process(raw_data)

        full_json_path.parent.mkdir(parents=True, exist_ok=True)
        with full_json_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def preprocess(self) -> None:
        pass

    def process(self, raw_data: list[dict[str, Any]]) -> Any:
        raise NotImplementedError
