`markdown
# Removing Outliers

## 📌 What Does Removal Mean?
Outliers are completely removed from the dataset.

## 🧪 Python Example
```python
df = df[(df['salary'] >= lower) & (df['salary'] <= upper)]]

Caution

Only remove if outliers are errors

Risky if outliers are meaningful
