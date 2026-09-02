import pandas as pd 
df= pd.DataFrame(pd.read_csv("F:/python/Pandas/raw_data.csv"))
df2=df.copy()
df2["tax"]=df2["income"].apply(lambda x : "10%"if x<50000 else "20%")
gender_map={"Male":"M","Female":"F","unknown":"U"}
df2["gender"]=df2["gender"].map(gender_map)
df2=df2.assign(new_income=df2["income"]*1.1)
df2["gender"]=df2["gender"].replace("NaN","Unknown")
print(df2)