import pandas as pd 
p = pd.Series([1,2,52,5,6],index=["dhruv","rajan","harsh","nikhil","shaurya"])
print(p["harsh"])

p["harsh"]=94549

print(p)

changedSeries = p.drop("nikhil")
print("changed series is ")

print(changedSeries)