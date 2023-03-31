import pandas as pd
from sqlalchemy import create_engine
db_connection_str='mysql+pymysql://prabha:Prabha23@localhost/myhcl'
db_connection=create_engine(db_connection_str)
df=pd.read_excel("C://mydataset//sample_pivot.xlsx",sheet_name='Sheet1',parse_dates=['Date'])
data=df.query('Sales>200')
east=df.where(df['Region']=='East')
task1=pd.crosstab(index=df['Region'],columns=df['Type'],values=df['Sales'],aggfunc='mean')
task2=pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
task3=pd.crosstab([df.Region,df.Date.dt.month],df.Type,values=df.Sales,margins=True,aggfunc='sum')
task4=pd.crosstab([df.Region,df.Date.dt.year],df.Type,values=df.Sales,margins=True,aggfunc='sum')
try:
    df.to_sql(name='mytable',con=db_connection)
except Exception as e:
    print(e)
# print(task1)
# print(task2)
# print(task3)
# print(task4)
print(data)
print(east)
cp=df.copy()
df.fillna(0,inplace=True)
print(df.isna().sum())
print(df.sort_values(['Region','Date'],ascending=False))