import pandas as pd
# data=[100,200,300,400,500]
# s=pd.Series(data)
# print(s)
# dates=pd.date_range(start='2023-02-01',end='2023-02-28')
# dates=pd.date_range(start='2023-02-01',periods=10,freq='D')
# dates=pd.date_range(start='2023-02-01',periods=10,freq='M')
# dates=pd.date_range(start='2023-02-01',periods=10,freq='Y')
# s=pd.Series(dates)
# print(s)

import random
# dates=pd.date_range(start='2023-02-01',end='2023-02-28')
# temp=[random.randint(28,31) for i in range(1,29)]
# day_temp=pd.Series(temp,index=dates)
# print(day_temp.iloc[2])
# print(day_temp.describe())

temp={'chennai':[random.randint(28,31) for i in range(1,10)],
      'Bangalore':[random.randint(27,30) for i in range(1,10)],
      'Vijayawada':[random.randint(27,30) for i in range(1,10)]}
humidity=[random.randint(30,35) for i in range(1,10)]
df=pd.DataFrame(temp)
df['humidity']=humidity
dropdata=df.drop('humidity',axis=1)
print(dropdata)
temp1=df.loc[8]
# print(df[:,'chennai'])
print(df.iloc[:,-1])
print(temp1)
rowdrop=df.drop(1,axis=0).reset_index(drop=True)
print(rowdrop)
df.rename(columns={'chennai':'chen'},inplace=True)
print(df)
