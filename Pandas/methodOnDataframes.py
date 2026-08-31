import pandas as pd 
df= pd.read_csv("F:\python\Pandas\sample.csv")
print(df.head(3))
print(df.tail())

print("sample")
print(df.sample(3))
print(df.info())
print(df.shape)
print(df.describe())
print(df.columns)
print(df.nunique())