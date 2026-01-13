```markdown
# Winsorization

## 📌 What is Winsorization?
Winsorization caps extreme values instead of removing them.

### Example
- Values above 99% → replaced by 99th percentile
- Values below 1% → replaced by 1st percentile

## 🧪 Python Example
```python
from scipy.stats.mstats import winsorize

df['salary_winsorized'] = winsorize(
    df['salary'],
    limits=[0.01, 0.01]
)

✅ Benefits

    Retains dataset size

    Reduces impact of extreme values





