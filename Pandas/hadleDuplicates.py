import pandas as pd 
df= pd.read_csv("F:/python/Pandas/raw_data.csv")
f=pd.DataFrame(df)
print(f)
print(f.duplicated())
print(f["country"].drop_duplicates()) # to make the changes i original data we use .drop_duplicates(inplace = true)