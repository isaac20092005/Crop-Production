import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week4\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

X = df[["Area 2010-11","Yield 2010-11"]]

y = df["Production 2010-11"]

print(X.head())
print(y.head())