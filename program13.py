import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week3\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

print("Median Yield 2010-11:")

print(df["Yield 2010-11"].median())