# HKDSE Statistics JSON
HKDSE is the university entrance exam in Hong Kong.
HKEAA has released [some HKDSE statistics in CSV format](https://data.gov.hk/en-datasets/provider/hkeaa)
from 2017 onwards.

The English versions of the CSV files are sanitized and converted to JSON for easier usage.

HKEAA uses inconsistent spellings and format across different CSV files.
HKEAA is a bad programmer. Don't be like HKEAA.

## Specification of `data/`
| Directory | Description | Availability | Corresponding table in [PDFs](https://www.hkeaa.edu.hk/en/HKDSE/assessment/exam_reports/exam_stat/) (2021 ver.) | Notes |
| --- | --- | --- | --- | --- |
| general/performance/level-2 | Attainment of Level 2 in different subject combinations* | 2017- | 3a | * `No. of candidates` is actually no. of candidates attempting 5+ Category A / B subjects |
| general/performance/best-5 | Attainment of levels in the best five subjects | 2017- | 3b | * |
| general/performance/university | No. of candidates meeting different university admission standards | 2017- | 3d | |
| general/performance/SEN | Performance of candidates with special needs | 2017- | 3g | allCandidates.json only |
| general/performance/top-levels/a | Attainment of top levels / grades in Category A subjects | 2017- | 3l-m | |
| general/performance/top-levels/a-b-c | Attainment of top levels / grades in Category A/B/C subjects | 2017- | 3l-m | |
| general/grade-point-distribution/2C-22222/best-5-chin-eng | Grade point distribution in the best five subjects (incl. Chinese Language & English Language) of candidates attaining 2+ in 5 subjects (incl. Chinese Language & English Language) | 2017- | 3c(ii) | * |
| general/grade-point-distribution/4C-3322/best-5 | See # below | 2017- | 3e(i) | * |
| general/grade-point-distribution/4C1X-33222/best-5 | See # below | 2019- | 3e(ii) | * |
| general/grade-point-distribution/4C1X-33222/4C1X | See # below | 2019- | 3e(ii) | * |
| general/grade-point-distribution/4C-3322/best-6 | See # below | 2019- | 3f(i) | ** `No. of candidates` is actually no. of candidates attempting 6+ Category A / B subjects |
| general/grade-point-distribution/4C2X-332233/best-6 | See # below | 2019- | 3f(ii) | ** |
| general/grade-point-distribution/4C2X-332233/4C2X | See # below | 2019- | 3f(ii) | ** |
| general/level-distribution/lang | Level distribution in Chinese Language & English Language | 2017- | 3h-i | Outer: Chinese Language <br> Inner: English Language |
| general/level-distribution/math | Level distribution in Mathematics Compulsory Part & Extended Part | 2017- | 3j-k | Outer: Compulsory Part <br> Inner: Extended Part |
| subjects/a | Performance in Category A subjects | 2017- | 5a-b | |
| subjects/b | Performance in Category B subjects except Applied Learning Chinese | 2017- | 5c-d | For 2017, performance in Applied Learning Chinese is included here instead of b-chinese |
| subjects/b-chinese | Performance in Applied Learning Chinese | 2018- | 5c-d | See *** below |
| subjects/c | Performance in Category C subjects | 2017- | 5e-f | |

| File | Description |
| --- | --- |
| daySchoolCandidates.json | Data for day school candidates |
| allCandidates.json | Data for all candidates |

Percentage data (except `chineseVersion`) is omitted since
it can be calculated as needed.

### Grade Point Conversion Table
| Category A Subject Level | Category B Subject Level | Points |
| --- | --- | --- |
| 5** | - | 7 |
| 5* | - | 6 |
| 5 | - | 5 |
| 4 | Attained with Distinction (II) | 4 |
| 3 | Attained with Distinction (I), Attained with Distinction | 3 |
| 2 | Attained | 2 |
| 1 | - | 1 |

### FAQ
> *** Why is Applied Learning Chinese separated from other Category B subjects starting from 2018?

Applied Learning Chinese is a Category B subject.
Attained with Distinction (I) & (II) were introduced to Category B subjects
except Applied Learning Chinese starting from 2018.

> \# How to understand the naming of `general/grade-point-distribution/**`?

The path is in the format `general/grade-point-distribution/[criteria]/[subject-combination]`.
The grade point distribution for each subject combination only includes candidates who meet the criteria.

| Subject Combination | Description |
| --- | --- |
| Best 5 | The five subjects with the highest grades |
| Best 6 | The six subjects with the highest grades |
| 4C | The four core subjects: Chinese Language, English Language, Mathematics (Compulsory Part) and Liberal Studies |
| 4C1X | 4C + one elective subject with the highest grades |
| 4C2X | 4C + two elective subjects with the highest grades |

| Criteria | Description |
| --- | --- |
| 4C-3322 | Attaining level 3+ in Chinese Language and English Language, and level 2+ in Mathematics (Compulsory Part) and Liberal Studies
| 4C1X-33222 | 3322 & attaining level 2+ in one elective subject |
| 4C2X-332233 | 3322 & attaining level 3+ in two elective subjects |

> Why is the data so disorganized?

info@hkeaa.edu.hk

## Sanitize Data
```bash
python -m sanitize
```
