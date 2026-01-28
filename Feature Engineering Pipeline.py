"""
Feature Engineering Pipeline Example
-----------------------------------
This script demonstrates common feature engineering steps
that can be reused in machine learning projects.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")  # Replace with your dataset path

# -----------------------------
# 2. Handle Missing Values
# -----------------------------

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Fill numerical columns with median
numerical_cols = df.select_dtypes(include=['number']).columns
for col in numerical_cols:
    df[col].fillna(df[col].median(), inplace=True)

# -----------------------------
# 3. Feature Creation
# -----------------------------

# Example: Age of item/house
if {'YrSold', 'YearBuilt'}.issubset(df.columns):
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']

# Example: Total area
if {'Length', 'Width'}.issubset(df.columns):
    df['TotalArea'] = df['Length'] * df['Width']

# -----------------------------
# 4. Handle Skewed Features
# -----------------------------
skewness = df[numerical_cols].skew()
skewed_cols = skewness[abs(skewness) > 1].index

for col in skewed_cols:
    if (df[col] > 0).all():
        df[col] = np.log(df[col])

# -----------------------------
# 5. Encode Categorical Variables
# -----------------------------
df = pd.get_dummies(df, drop_first=True)

# -----------------------------
# 6. Feature Scaling
# -----------------------------
scaler = StandardScaler()
numerical_cols = df.select_dtypes(include=['number']).columns

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# -----------------------------
# 7. Feature Selection (Remove High Correlation)
# -----------------------------
corr_matrix = df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

high_corr = [column for column in upper.columns if any(upper[column] > 0.9)]
df.drop(columns=high_corr, inplace=True)

# -----------------------------
# 8. Train/Test Split
# -----------------------------
target_column = "SalePrice"  # Change to your target column

if target_column in df.columns:
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # -----------------------------
    # 9. Train Simple Model
    # -----------------------------
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Model training complete ✅")
    print("Train Score:", model.score(X_train, y_train))
    print("Test Score:", model.score(X_test, y_test))
else:
    print(f"Target column '{target_column}' not found in dataset.")
