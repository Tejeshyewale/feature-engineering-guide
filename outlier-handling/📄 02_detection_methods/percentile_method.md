
---

## 📄 `02_detection_methods/percentile_method.md`

```markdown
# Percentile Method for Outlier Detection

## 📌 What is Percentile Method?
Outliers are values that lie outside a chosen percentile range.

### Common Thresholds
- Lower: 1st percentile
- Upper: 99th percentile

## 🧪 Python Example
```python
lower = df['salary'].quantile(0.01)
upper = df['salary'].quantile(0.99)

outliers = df[(df['salary'] < lower) |
              (df['salary'] > upper)]
When to Use

Large datasets

Flexible control over outlier limits
