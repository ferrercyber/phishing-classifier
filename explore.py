import pandas as pd

df = pd.read_csv('emails.csv')

print(df.head())
print('Shape:', df.shape)
print(df['label'].value_counts())
print(df.isnull().sum())

df.dropna(inplace=True)
print('After cleanup:', df.shape)
