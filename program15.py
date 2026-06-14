import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week3\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

plt.hist(df["Yield 2010-11"], bins=10)

plt.title("Yield Distribution 2010-11")

plt.show()