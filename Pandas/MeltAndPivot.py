import pandas as pd 
df=pd.DataFrame(pd.read_csv("F:/python/Pandas/raw_data.csv"))
print(df)
print("\n\n\n")
melted_df=df.melt(
    id_vars=["name","age","country"],
    value_vars=["gender","income"],
    var_name="new_col",
    value_name="value"
)
print(melted_df)

print("\n\n")

melted_df = melted_df.drop_duplicates()

pivoted_df = melted_df.pivot(
    index=["name", "age"],
    columns="new_col",
    values="value"
)
print(pivoted_df)