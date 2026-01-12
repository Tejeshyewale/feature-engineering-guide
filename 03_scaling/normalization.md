# Normalization

Normalization scales numerical features into a fixed range,
usually between 0 and 1.

---

## Formula
X_normalized = (X - X_min) / (X_max - X_min)

---

## When to use
- Features have different ranges
- Distance-based models are used

---

## Common algorithms
- KNN
- K-Means
- Neural Networks

---

## Advantages
- Maintains relative scale
- Improves convergence

---

## Disadvantages
- Sensitive to outliers

---

## One-liner
Normalization rescales data into a fixed range, usually 0 to 1.
