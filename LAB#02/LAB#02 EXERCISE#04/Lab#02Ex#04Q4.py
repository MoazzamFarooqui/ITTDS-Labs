import pandas as pd
df_customerfeedback=pd.read_csv('customer_feedback.csv')
df_customerfeedback=df_customerfeedback.dropna(subset=['comment'])
print(df_customerfeedback)