import pandas as pd 
df=pd.read_csv("F:\python\Pandas\globalAirQuality.csv")
f= pd.DataFrame(df)
print(df.columns)
print(f[["city","aqi"]])
print(f.loc[2])
print(f.loc[0:2])


print(f.iloc[0:2])
print(f.iloc[0:2,0:4])
print(f.at[0,"city"])
print(f.iat[0,3])