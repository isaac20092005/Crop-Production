import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week2\dataset\datafile 2.csv")

top = df.sort_values("Production 2010-11", ascending=False).head(10)

plt.bar(top["Crop"], top["Production 2010-11"])
plt.xticks(rotation=90)
plt.title("Top Crops by Production 2010-11")
plt.show()