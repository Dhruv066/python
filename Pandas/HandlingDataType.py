import pandas as pd 
df= pd.read_csv("F:/python/Pandas/raw_data.csv")
f=pd.DataFrame(df)
print(f.dtypes)

f2=f.copy()
f2=f2["age"].fillna(0)
 
f2["age"]=f2.astype("int64")
# f2["age"] = f2["age"].astype("int64")
print(df.columns.tolist())

df2= pd.read_csv("F:/python/Pandas/globalAirQuality.csv")
f3=pd.DataFrame(df2)
print(f3.columns)

f3["timestamp"]=pd.to_datetime(f3["timestamp"])

print(f3["timestamp"].dtypes)