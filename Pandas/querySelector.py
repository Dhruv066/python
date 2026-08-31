import pandas as pd 
df= pd.read_csv("F:\python\Pandas\globalAirQuality.csv")
f= pd.DataFrame(df)
print(f.columns)
print(f.query("temperature>30 & aqi>100 & city=='New York'")[["city","temperature"]])