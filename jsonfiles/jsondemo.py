import pandas as pd
df=pd.read_csv(filepath_or_buffer="C:\mydataset/tips.csv")
js=df.to_json("C:/mydataset/jsondemo.json",orient="records")
print(js)