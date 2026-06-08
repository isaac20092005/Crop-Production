import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week1\dataset\datafile.csv")

df.iloc[:,0].value_counts().head(5).plot(kind='bar')

plt.title("Top 5 Values")

plt.show()