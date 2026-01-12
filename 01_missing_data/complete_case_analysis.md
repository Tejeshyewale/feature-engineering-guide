# Complete Case Analysis (CCA)

Complete Case Analysis removes all rows that contain at least one missing value.

---

## How it works
- If a row has any missing value, it is deleted
- Only complete rows are used for analysis

---

## When to use
- Missing data is very small
- Data is MCAR
- Dataset is large

---

## Advantages
- Very simple
- No imputation bias
- Easy to implement

---

## Disadvantages
- Data loss
- Reduced sample size
- Biased if data is not MCAR

---

## One-liner
Complete Case Analysis removes all observations with missing values.
