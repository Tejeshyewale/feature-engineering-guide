# One-Hot Encoding

One-Hot Encoding converts categorical variables into multiple binary columns.

---

## How it works
Each category becomes a new column with values:
- 1 → category present
- 0 → category absent

Example:
City → Mumbai, Pune

| City_Mumbai | City_Pune |
|------------|-----------|
| 1 | 0 |
| 0 | 1 |

---

## When to use
- Categorical data is **nominal**
- No natural order exists

---

## Advantages
- No false ordering
- Works well with linear models

---

## Disadvantages
- Increases dimensionality
- Not efficient for high-cardinality data

---

## One-liner
One-hot encoding converts categories into binary indicator columns.
