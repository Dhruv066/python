import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("F:/python/pandas/raw_data.csv")
df.plot()
df["age"].hist()

plt.show()  # This line actually renders the plot window
