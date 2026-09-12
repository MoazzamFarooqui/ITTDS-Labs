import pandas as pd
df=pd.read_csv('employee.csv')
print(df[['Employee Name','Department']].head())

