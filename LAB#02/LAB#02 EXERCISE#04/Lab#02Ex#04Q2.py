import pandas as pd
df_customerfeedback=pd.read_csv('customer_feedback.csv')
df_customerfeedback['rating']=df_customerfeedback['rating'].fillna(df_customerfeedback['rating'].mean())
print(df_customerfeedback)
