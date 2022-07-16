import os
import re
from typing import Optional



def remove_duplicate_space(s) -> str:
    return re.sub(r"\s+", " ", s.strip())


def get_years() -> list[str]:
    res = os.listdir("raw")
    res.sort(key=int)
    return res


def int_if_not_none(s: Optional[str]) -> Optional[int]:
    return None if s is None else int(s)
