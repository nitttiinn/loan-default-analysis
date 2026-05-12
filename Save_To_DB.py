from sqlalchemy import create_engine,text
import pandas as pd

#1. Load Analyzed Data 
df = pd.read_csv('Data/Analyzed_Loan_Data.csv')
#print(f'Loaded Data: {df.shape}')   

#2. Create DATABASE:
engine = create_engine('mysql+pymysql://root:root@localhost:3306');
#print("Connect to SQLAlchemy")

with engine.connect() as conn:
        conn.execute(text('CREATE DATABASE IF NOT EXISTS loan_analysis_db'))
        conn.commit()
        print('Database Created✅')

#3. Connect to Database:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/loan_analysis_db')
print("Connect to Database ✅")


#4.  Save Data to MySQL
df.to_sql('loan_data',engine,if_exists='replace',index=False)
print(f'Data Saved to MySQL! ✅')
print(f'Total rows saved: {len(df)}')