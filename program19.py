import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Agri_Project_Week4\dataset\datafile 2.csv")

df.columns = df.columns.str.strip()

X = df[["Area 2010-11","Yield 2010-11"]]
y = df["Production 2010-11"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(X_train,y_train)

print("Model Trained Successfully")