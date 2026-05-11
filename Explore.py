import pandas as pd

#1. load data:
df = pd.read_csv("Data/Loan_Default.csv")

#2. Basic Info:
print("="*50)
print("DATASET INFO")
print(df.info())

print("="*50)
print("DATASET SHAPE: ")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("="*50)
print("MISSING VALUES PER COLUMN:")
missing = df.isnull().sum()
missing_percent = (df.isnull().sum()/len(df)*100).round(2)
missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %' : missing_percent })
print(missing_df[missing_df['Missing Count']>0])

print("="*50)
print("DEFAULT RATE:")
default_rate = df['Status'].value_counts()
default_percent = df['Status'].value_counts(normalize=True)*100
print(f"Total Loans: {len(df)}")
print(f"Defaulted: {default_rate[1]}({default_percent[1].round(2)}%)")
print(f"Paid Back: {default_rate[0]}({default_percent[0].round(2)}%)")

print("="*50)
print("DEFAULT RATE BY AGE:")
print(df.groupby('age')['Status'].mean().round(3)*100)

print("="*50)
print("DEFAULT RATE BY REGION:")
print(df.groupby('Region')['Status'].mean().round(3)*100)

print("="*50)
print("DEFAULT RATE BY GENDER:")
print(df.groupby('Gender')['Status'].mean().round(3)*100)

print("="*50)
print("STATISTICAL SUMMARY:")
print(df[['loan_amount','income','Credit_Score','LTV']].describe())
