
# MCAR, MAR, MNAR – Missing Data Mechanisms

Before handling missing values, we must understand **why the data is missing**.

There are three types of missing data mechanisms.

---

## 1. MCAR – Missing Completely At Random

Data is missing **purely by chance** and is not related to any variable.

Example:
- System crash
- Random data loss

Key points:
- No pattern in missing data
- No bias introduced

Safe methods:
- Complete Case Analysis
- Mean / Mode Imputation

One-liner:
MCAR means data is missing randomly and is unrelated to any variable.

---

## 2. MAR – Missing At Random

Missingness depends on **another observed variable**, not on the missing value itself.

Example:
- Income missing for students
- Marks missing for absent students

Key points:
- Pattern exists
- Depends on known data

Safe methods:
- KNN Imputer
- MICE
- Group-based imputation

One-liner:
MAR means missingness depends on other observed variables.

---

## 3. MNAR – Missing Not At Random

Missingness depends on **the value itself**.

Example:
- High-income people hiding income
- Low marks not reported

Key points:
- Strong bias
- Hardest to handle

Handling:
- Domain knowledge
- Missing indicator
- Special modeling

One-liner:
MNAR means data is missing because of the value itself.
