import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#1. Make Charts folder:
os.makedirs('Charts',exist_ok=True)

#2. Load Analyzed Data:
df = pd.read_csv("Data/Analyzed_Loan_Data.csv")

#3. Set Style:
sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 100

#4. CHART 1 -> Default Rate by CREDIT SCORE GROUP
credit_default = df.groupby('Credit_Score_Group')['Status'].mean().mul(100).sort_values(ascending=False)

plt.figure(figsize=(10,4))
bars = plt.bar(credit_default.index,credit_default.values, color=['red', 'orange', 'yellow', 'lightgreen', 'green'])
plt.title('Default Rate By Credit Score Group',fontsize = 14,fontweight = 'bold')
plt.xlabel('Credit Score Group')
plt.ylabel('Default Rate %')
plt.ylim(0,credit_default.max()+5)

# Show Percentage on top of each bar:
for bar,val in zip(bars,credit_default.values):
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.5,f'{val:.1f}%',ha = 'center',fontsize = 10,fontweight = 'bold')

plt.tight_layout()
plt.savefig('Charts/chart1_Credit_Score.png')
# plt.show()

# Chart 2 -> Default Rate by Loan Purpose:
loan_purpose_default = df.groupby('loan_purpose')['Status'].mean().mul(100).sort_values(ascending=False)

plt.figure(figsize=(10,5))
bars = plt.bar(loan_purpose_default.index,loan_purpose_default.values,color = 'coral')
plt.title('Default Rate by Loan Purpose',fontsize = 14,fontweight = 'bold')
plt.xlabel('Loan Purpose')
plt.ylabel('Default Rate %')
plt.ylim(0,loan_purpose_default.max()+5)

for bar,val in zip(bars,loan_purpose_default.values):
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.5,
             f'{val:.1f}%',ha= 'center',fontsize=10,fontweight = 'bold')
    
plt.tight_layout()
plt.savefig('Charts/chart2_Loan_Purpose.png')
#plt.show()

# Chart 3 -> Default Rate by Income Group:
income_order = ['Very Low','Low','Medium','High','Very High']
income_default = df.groupby('income_group')['Status'].mean().mul(100)
income_default = income_default.reindex(income_order)

plt.figure(figsize=(10,5))
bars = plt.bar(income_default.index,income_default.values,color = ['red','orange','green','lightgreen','orange'])
plt.title('Default Rate by Income Group',fontsize = 14,fontweight = 'bold')
plt.xlabel('Income Group')
plt.ylabel('Default Rate %')
plt.ylim(0,income_default.max()+5)

for bar,val in zip(bars,income_default.values):
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.5,
             f'{val:.1f}%',ha= 'center',fontsize=10,fontweight = 'bold')
    
plt.tight_layout()
plt.savefig('Charts/chart3_Income_Group.png')
#plt.show()

# Chart 4 -> Default Rate by Loan Amount Group:
loan_order = income_order = ['Very Small','Small','Medium','Large','Very Large']
loan_amount_default = df.groupby('loan_amount_group')['Status'].mean().mul(100)
loan_amount_default = loan_amount_default.reindex(loan_order)

plt.figure(figsize=(10,5))
bars = plt.bar(loan_amount_default.index,loan_amount_default.values,color = ['red','orange','green','lightgreen','orange'])
plt.title('Default Rate by Loan Amount',fontsize = 14,fontweight = 'bold')
plt.xlabel('Loan Amount Group')
plt.ylabel('Default Rate %')
plt.ylim(0,loan_amount_default.max()+5)

for bar,val in zip(bars,loan_amount_default.values):
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.5,
             f'{val:.1f}%',ha= 'center',fontsize=10,fontweight = 'bold')
    
plt.tight_layout()
plt.savefig('Charts/chart3_Loan_Amount.png')
plt.show()