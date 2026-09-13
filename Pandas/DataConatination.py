import pandas as pd 
df= pd.DataFrame({
    "name":["ankit","rahul","vineet","khushi"],
    "age":[12,36,43,13],
    "id":[101,102,103,104]
})

df2=pd.DataFrame({
    "Salary":[120000,130000,90000,140000],
    "company":["HCL","BAjaj","Amazon","Flipkart"],
    "id":[101,102,103,104]
})

df_concated=pd.concat([df,df2],ignore_index=True,axis=1)
print(df_concated)
