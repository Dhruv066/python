import pandas as pd 
df=pd.DataFrame(pd.read_csv("F:/python/Pandas/raw_data.csv"))
print(df)

# print(df.groupby("country")["income"].max())
# print(df.groupby("country")["income"].min())
# print(df.groupby("country")["income"].mean())

# print(df.groupby("gender")["income"].mean())
# print(df.groupby("gender")["income"].max())

print(df.groupby("country")["income"].agg(["mean","max","min"])) #.aggregate do same as agg

print(df.groupby("country")["income"].agg(Mean_sal="mean",Max_Sal="max",Min_Sal="min"))

print(df.groupby("country").agg(
    {

        "income":"mean",
        "age":"mean"
    }
))

print("\n\n")

print(df.groupby("country").agg(
    max_sal=("income","max"),
    avg_age=("age","mean")

))