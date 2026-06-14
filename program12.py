import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week3\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

print("Mean Production 2010-11:")

print(df["Production 2010-11"].mean())