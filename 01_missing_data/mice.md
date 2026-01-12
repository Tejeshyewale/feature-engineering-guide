# MICE – Multiple Imputation by Chained Equations

MICE is an iterative, model-based imputation technique.

---

## How it works
- Each feature with missing values is modeled using other features
- Imputation happens in cycles
- Process is repeated multiple times

---

## Advantages
- Preserves relationships
- Statistically sound
- Handles MAR well

---

## Disadvantages
- Slow
- Computationally expensive
- Complex to explain

---

## When to use
- Medium-sized datasets
- Strong feature relationships
- Statistical correctness is important

---

## One-liner
MICE imputes missing values by iteratively modeling each feature.
