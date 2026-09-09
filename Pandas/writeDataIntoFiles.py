import pandas as pd 
df = pd.read_csv("F:/python/Pandas/raw_data.csv")
df= pd.DataFrame(df)
print(df)

df= df.drop_duplicates()
df=df.sort_values("income")
df=df.reset_index(drop=True)
print("\n\n\n")
print(df)

df.to_excel("raw_data.xlsx")