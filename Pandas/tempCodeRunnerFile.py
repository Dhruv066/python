"10%"if x<50000 else "20%")
gender_map={"Male":"M","Female":"F","unknown":"U"}
df2["gender"]=df2["gender"].map(gender_map)
df2=df2.assign(new_income=df2["income"]*1.1)
df2["gender"]=df2["gender"].replace("NaN","Unknown")
df2.columns=["Id","Name","Age","Country","Gender","Income","Tax","New_income"]
df2.rename({"Income":"Salary"})
print(df2)