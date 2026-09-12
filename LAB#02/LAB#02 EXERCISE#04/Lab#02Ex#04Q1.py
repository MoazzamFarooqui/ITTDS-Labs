import pandas as pd
df_customerfeedback=pd.read_csv('customer_feedback.csv')
print(df_customerfeedback.isnull().sum())

