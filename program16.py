import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week4\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

encoder = LabelEncoder()

df["Crop"] = encoder.fit_transform(df["Crop"])

print(df.head())