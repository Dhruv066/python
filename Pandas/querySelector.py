import pandas as pd 
df= pd.read_csv("F:\python\Pandas\globalAirQuality.csv")
f= pd.DataFrame(df)
print(f.columns)
aqiVal= 25
print(f.query("temperature>@aqiVal & aqi>100 & city=='New York'")[["city","temperature"]])