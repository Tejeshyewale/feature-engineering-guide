# Arbitrary Value Imputation

Arbitrary value imputation replaces missing values with a fixed value
that clearly represents missingness.

---

## Examples
- Numerical: -1, 999
- Categorical: "Unknown", "Missing"

---

## Why use it
- Missingness itself is informative
- Easy to implement

---

## Advantages
- Preserves missing information
- Works well with tree-based models

---

## Disadvantages
- Can distort scale
- Not suitable for distance-based models

---

## One-liner
Arbitrary value imputation replaces missing values with a predefined constant.
