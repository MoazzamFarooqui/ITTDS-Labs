import pandas as pd
df_emp=pd.read_csv('employee.csv')
print(df_emp[df_emp['SALARY']>50000])

