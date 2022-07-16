# HKDSE Statistics JSON
HKDSE is the university entrance exam in Hong Kong.
HKEAA has released [some HKDSE statistics in CSV format](https://data.gov.hk/en-datasets/provider/hkeaa)
from 2017 onwards.

The English versions of the CSV files are sanitized and converted to JSON for easier usage.

HKEAA uses inconsistent spellings and format across different CSV files.
HKEAA is a bad programmer. Don't be like HKEAA.

## Specification of `data/`
| Directory | Description | Availability | Corresponding table in [PDFs](https://www.hkeaa.edu.hk/en/HKDSE/assessment/exam_reports/exam_stat/) (2021 ver.) | Done? |
| --- | --- | --- | --- | --- |
| general/performance/level-2 | Attainment of Level 2 in different subject combinations* | 2017- | 3a | Yes |
| general/performance/best-5 | Attainment of levels in the best five subjects* | 2017- | 3b | Yes |
| general/performance/university | No. of candidates meeting different university admission standards | 2017- | 3d | Yes |
| general/performance/SEN | Performance of candidates with special needs (allCandidates.json only) | 2017- | 3g | Yes |
| general/performance/top-levels/a | Attainment of top levels / grades in Category A subjects | 2017- | 3l-m | No |
| general/performance/top-levels/a-b-c | Attainment of top levels / grades in Category A/B/C subjects | 2017- | 3l-m | No |
| general/grade-point-distribution/2C-22222/best-5-chin-eng | Grade point distribution in the best five subjects (incl. Chinese Language & English Language) of candidates attaining 2+ in 5 subjects (incl. Chinese Language & English Language)* | 2017- | 3c(ii) | Yes |
| general/grade-point-distribution/4C-3322/best-5 | See # * | 2017- | 3e(i) | Yes |
| general/grade-point-distribution/4C1X-33222/best-5 | See # * | 2019- | 3e(ii) | Yes |
| general/grade-point-distribution/4C1X-33222/4C1X | See # * | 2019- | 3e(ii) | Yes |
| general/grade-point-distribution/4C-3322/best-6 | See # ** | 2019- | 3f(i) | Yes |
| general/grade-point-distribution/4C2X-332233/best-6 | See # ** | 2019- | 3f(ii) | Yes |
| general/grade-point-distribution/4C2X-332233/4C2X | See # ** | 2019- | 3f(ii) | Yes |
| general/level-distribution/lang | Level distribution in Chinese Language & English Language | 2017- | 3h-i | No |
| general/level-distribution/math | Level distribution in Mathematics Compulsory Part & Extended Part | 2017- | 3j-k | No |
| subjects/a | Performance in Category A subjects | 2017- | 5a-b | Yes |
| subjects/b | Performance in Category B subjects except Applied Learning Chinese | 2017- *** | 5c-d | Yes |
| subjects/b-chinese | Performance in Applied Learning Chinese | 2018- *** | 5c-d | Yes |
| subjects/c | Performance in Category C subjects | 2017- | 5e-f | Yes |

| File | Description |
| --- | --- |
| daySchoolCandidates.json | Data for day school candidates |
| allCandidates.json | Data for all candidates |

Percentage data (except Chinese Version %) is omitted since
it can be calculated as needed.

\* `No. of candidates` is actually no. of candidates attempting 5+ Category A / B subjects <br>
\*\* `No. of candidates` is actually no. of candidates attempting 6+ Category A / B subjects

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
> Why is `subjects/2017/b-chinese` missing?

\*\*\* Applied Learning Chinese is a Category B subject.
For 2017, performance in Applied Learning Chinese is included in `subjects/2017/subjects/b`.
However, Attained with Distinction (I) & (II) were introduced to Category B subjects
except Applied Learning Chinese starting from 2018. Hence the separation of
Applied Learning Chinese from other Category B subjects thereafter.

> How to understand the naming of `general/grade-point-distribution/**`?

\# The path is in the format `general/grade-point-distribution/[criteria]/[subject-combination]`.
The grade point distribution for each subject combination only includes candidates who meet the criteria.

| Criteria | Description |
| --- | --- |
| 3322 | Attaining level 3+ in Chinese Language and English Language, and level 2+ in Mathematics (Compulsory Part) and Liberal Studies
| 33222 | 3322 & attaining level 2+ in one elective subject |
| 332233 | 3322 & attaining level 3+ in two elective subjects |

| Subject Combination | Description |
| --- | --- |
| Best 5 | The five subjects with the highest grades |
| Best 6 | The six subjects with the highest grades |
| 4C | The four core subjects: Chinese Language, English Language, Mathematics (Compulsory Part), Liberal Studies |
| 4C+1X | 4C + one elective subject with the highest grades |
| 4C+2X | 4C + two elective subjects with the highest grades |

> Why is the data so disorganized?

info@hkeaa.edu.hk

## Sanitize Data
```bash
python -m sanitize
```
