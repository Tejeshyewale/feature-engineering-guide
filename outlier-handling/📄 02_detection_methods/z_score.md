# Z-Score Method for Outlier Detection

## 📌 What is Z-Score?
Z-score measures how many **standard deviations** a value is from the mean.

### Formula

Z = (x - mean) / standard deviation


### Rule
- If `|Z| > 3`, the value is considered an outlier.

## 🧪 Python Example
```python
from scipy import stats

df['z_score'] = stats.zscore(df['salary'])
outliers = df[df['z_score'].abs() > 3]

✅ When to Use

Data is normally distributed

Dataset has no extreme skew

