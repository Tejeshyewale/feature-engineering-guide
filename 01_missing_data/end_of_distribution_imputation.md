# End of Distribution Imputation

End of distribution imputation replaces missing values with extreme values
from the tail of the data distribution.

---

## How values are chosen
- Mean ± 3 × Standard Deviation
- Very small or very large values

---

## Why use it
- Keeps missingness signal
- Separates missing values from normal values

---

## Advantages
- Preserves dataset size
- Useful for tree-based models

---

## Disadvantages
- Distorts distribution
- Not suitable for linear models

---

## One-liner
End of distribution imputation uses extreme tail values to replace missing data.
