import pandas as pd
import numpy as np

#1. Load Cleaned Data:
df = pd.read_csv('Data/cleaned_Loan_Data.csv')
print(f"Loaded Cleaned Data: {df.shape}")
print("="*50)

# Analysis 1 - Default Rate by Credit Score Group
# 1. Create Credit Score Groups:
df['Credit_Score_Group'] = pd.cut(
    df['Credit_Score'],
    bins = [0,580,670,740,800,9000],
    labels = ['Poor','Fair','Good','Very Good','Exceptional']
    )
#2. Default Rate:
credit_default = df.groupby('Credit_Score_Group')['Status'].mean()*100
credit_default = credit_default.sort_values(ascending=False)
print("DEFAULT RATE BY CREDIT SCORE:")
print(credit_default.round(2))

# Analysis 2 -> Default Rate by Loan Purpose:
loan_purpose_default = df.groupby('loan_purpose')['Status'].mean()*100
loan_purpose_default = loan_purpose_default.sort_values(ascending=False)

print("="*50)
print("DEFAULT RATE BY LOAN PURPOSE:")
print(loan_purpose_default.round(2))

# Analysis 3 -> Default Rate by Income Group:
df['income_group'] = pd.cut(
    df['income'],
    bins = [0,3000,6000,10000,20000,999990],
    labels = ['Very Low','Low','Medium','High','Very High']
)
income_group_default = df.groupby('income_group')['Status'].mean().sort_values(ascending=False)*100

print("="*50)
print("DEFAULT RATE BY INCOME GROUP:")
print(income_group_default.round(2))

# Analysis 4 - Default Rate by Loan Amount Group:
df['loan_amount_group'] = pd.cut(
    df['loan_amount'],
    bins = [0,100000,250000,500000,999999,9999999],
    labels = ['Very Small','Small','Medium','Large','Very Large']
)

loan_amount_default = df.groupby('loan_amount_group')['Status'].mean().sort_values(ascending=False)*100

print("="*50)
print("DEFAULT RATE BY LOAN AMOUNT:")
print(loan_amount_default.round(2))

# Analysis 5 - LTV vs Default Rate:
df['ltv_group'] = pd.cut(
    df['LTV'],
    bins = [0,60,80,90,100,9999],
    labels = ['Very Low','Low','Medium','High','Very High']
)

ltv_default = df.groupby('ltv_group')['Status'].mean().sort_values(ascending=False)*100

print("="*50)
print("DEFAULT RATE BY LTV GROUP:")
print(ltv_default.round(2))

# Analysis 6 - Summary Statistics By Default Status
print("="*50)
print("AVERAGE STATS - DEFAULT VS PAID BACK")
summary = df.groupby('Status')[['loan_amount','income','Credit_Score','LTV']].mean().round(2)
summary.index = ['Paid Back','Defaulted']
print(summary)

# Save Analysis Results:
df.to_csv('Data/Analyzed_Loan_Data.csv',index = False,dirs_exist_ok= True)
print("\nAnalysis Saved!✅")