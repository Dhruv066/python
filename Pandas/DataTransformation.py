import pandas as pd 
df= pd.DataFrame(pd.read_csv("F:/python/Pandas/raw_data.csv"))
df2=df.copy()
df2["tax"]=df2["income"].apply(lambda x : "10%"if x<50000 else "20%")
gender_map={"Male":"M","Female":"F","unknown":"U"}
df2["gender"]=df2["gender"].map(gender_map)
df2=df2.assign(new_income=df2["income"]*1.1)
df2["gender"]=df2["gender"].replace("NaN","Unknown")
df2.columns=["Id","Name","Age","Country","Gender","Income","Tax","New_income"]
df2=df2.rename(columns={"Income":"Salary"}) #renames the columns name 
df2=df2.rename(index={1:"First",2:"second"})#rename the index 
df2["Age"]=df2["Age"].fillna(50) #fills the NaN values with 50
#print(df2.sort_values("Age"))#it soted the vakues on the basis of age



#print(df2.sort_values(["Salary","Age"])) #here the values will be sorted first on the  basis of the salary and if the salary is same then values will gwt sorted on tha basis of the age 
sorted_df=df2.sort_values("Salary")
sorted_df=sorted_df.reset_index()
print(sorted_df)