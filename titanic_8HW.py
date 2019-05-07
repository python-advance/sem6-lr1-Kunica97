import pandas as pd

df = pd.read_csv('train.csv')
md = df['Fare'].median()
mn = df['Fare'].mean()
print(md, mn)