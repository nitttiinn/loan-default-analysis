import pandas as pd
import numpy as np

#1. Load Data:
df = pd.read_csv("Data/Loan_Default.csv")
print(f"Before Cleaning: {df.shape}")

# Step 1 -> Drop rows with very few missing values:
df = df.dropna(subset = ['age','loan_purpose','term','Neg_ammortization'])
print(f"After Dropping Few Missing Rows: {df.shape}")

# Step 2 -> Fill Numerical columns with mean:
numerical_cols=[
    'rate_of_interest',
    'Interest_rate_spread',
    'Upfront_charges',
    'property_value',
    'income',
    'LTV',
    'dtir1'
]

for col in numerical_cols:
    mean_value = df[col].mean()
    df[col] = df[col].fillna(mean_value)
    print(f"Filled {col} with Mean: {mean_value.round(2)}")

# Step 3 -> Fill Categorical columns with Unknown:
print("="*20)
categorial_cols = ['loan_limit','approv_in_adv']

for col in categorial_cols:
    df[col] = df[col].fillna('Unknown')
    print(f"Filled {col} with Unknown")

# Step 4 -> Select only columns we need:
print("="*50)
columns_we_need =[
    'loan_amount',
    'income',
    'Credit_Score',
    'age',
    'Region',
    'Gender',
    'loan_purpose',
    'rate_of_interest',
    'property_value',
    'LTV',
    'Status'
]

df = df[columns_we_need]
print(f"\nAfter Selecting Important Columns: {df.shape}")

# Step 5 -> Verify no missing values left:
print('\nMissing Values after cleaning:')
print(df.isnull().sum())

# Step 6 -> Save cleaned Data:
df.to_csv('Data/Cleaned_Loan_Data.csv',index=False)
print("\Cleaned Data Saved!✅")