
## 📄 `03_handling_methods/transformation.md`

```markdown
# Data Transformation for Outliers

## 📌 What is Transformation?
Transforms data to reduce the effect of outliers.

### Common Transformations
- Log
- Square root

## 🧪 Python Example
```python
import numpy as np

df['salary_log'] = np.log(df['salary'])

✅ When to Use

    Highly skewed data

    Financial datasets
