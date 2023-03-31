import pandas as pd
def check_data(dataframe):
    count_null = 0
    count_row = 1
    for i in range(2,len(df.index)+1):
        d=df.isna
        if d==True:
            count_null+=1
        else:
            count_row+=1
    return count_null,count_row
# df=pd.read_excel("C://mydataset//master_data.xlsx")
df=pd.read_excel("C://mydataset//daily_data.xlsx")
print(check_data(df))



