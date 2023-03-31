import pandas as pd
from functools import reduce
from sqlalchemy import create_engine
db_connection_str='mysql+pymysql://prabha:Prabha23@localhost/myhcl'
db_connection=create_engine(db_connection_str)
sheet_name=["Jan","Feb","Mar","April","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
l=[]
# jan=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Jan')
# feb=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Feb')
# mar=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Mar')
# apr=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='April')
# may=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='May')
# jun=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Jun')
# jul=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Jul')
# aug=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Aug')
# sep=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Sep')
# oct=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Oct')
# nov=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Nov')
# dec=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name='Dec')
for i in sheet_name:
    df=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name=i,usecols=['Date','Prod_id','Price','Qty'])
    l.append(df)
data=reduce(lambda left,right:pd.merge(left,right,on="Prod_id",how='inner'),l)
# d=pd.crosstab(index=df.Prod_id,columns=df.Prod_name,values=df.Qty,aggfunc='sum',dropna=False)
# print(data)
data.to_excel("C://excel_data//month_report.xlsx")
try:
    data.to_sql(name='month_table2',con=db_connection,if_exists='replace')
except Exception as e:
    print(e)
print(data)
# res=jan.merge(feb,on="Prod_id").merge(mar,on="Prod_id").merge(apr,on="Prod_id")
# print(res)
# df=pd.read_excel("C://mydataset//monthly_report.xlsx",sheet_name=sheet_name)
# print(df.get('Jan'))