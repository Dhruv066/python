import pandas as pd
df= pd.read_csv("F:/python/Pandas/raw_data.csv")
f=pd.DataFrame(df)
print(f)
print(f.isnull())
print(f.isnull().sum())# it returns the total count of the null values in each columns 
print(f["age"].isnull())    # it returns the all null values in age column
print(f.dropna())# drop all the colums that have null values 
print(f.fillna(0))  # fills the null value with the provided value 
print(f.ffill()) #fills the above value to at null place
# print(f.bfill()) #fills the below value to at null place