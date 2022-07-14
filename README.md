# HKDSE Category A Subject Statistics JSON
HKDSE is the university entrance exam in Hong Kong.
HKEAA has released [HKDSE statistics in CSV format](https://data.gov.hk/en-datasets/provider/hkeaa)
from 2017 onwards.

The English versions of some CSV files are
sanitized and converted to JSON for easier usage.

HKEAA uses inconsistent spellings and format across different CSV files.
HKEAA is a bad programmer. Don't be like HKEAA.

## Specification
| File | Description |
| --- | --- |
| a.json | Performance in Category A subjects (day school candidates) |
| b.json | Performance in Category A subjects (all candidates) |

Percentage data (except Chinese Version %) is omitted since
it can be calculated by `Number / No. sat` as needed.

Sample subject data:
```json
{
    "subject": "Mathematics",
    "subcategory": "Compulsory Part",
    "male": {
        "noEntered": 21303,
        "noSat": 20835,
        "chineseVersion": 41.7,
        "5**": 438,
        "5*+": 1609,
        "5+": 3601,
        "4+": 8468,
        "3+": 12198,
        "2+": 16809,
        "1+": 19224,
        "U": 1611
    },
    "female": {
        "noEntered": 21000,
        "noSat": 20662,
        "chineseVersion": 32.9,
        "5**": 159,
        "5*+": 873,
        "5+": 2554,
        "4+": 7904,
        "3+": 12227,
        "2+": 17145,
        "1+": 19410,
        "U": 1252
    },
    "total": {
        "noEntered": 42303,
        "noSat": 41497,
        "chineseVersion": 37.3,
        "5**": 597,
        "5*+": 2482,
        "5+": 6155,
        "4+": 16372,
        "3+": 24425,
        "2+": 33954,
        "1+": 38634,
        "U": 2863
    }
}
```
