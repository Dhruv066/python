import pandas as pd 
df= pd.read_csv("F:\python\Pandas\globalAirQuality.csv")
f=pd.DataFrame(df)
print(df[(df["aqi"]>50)& (df["city"]=="New York")])
print(f.columns)
print(df[(df["aqi"]>50)& (df["temperature"]>20)])