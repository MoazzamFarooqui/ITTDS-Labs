import pandas as pd
df_emp=pd.read_csv('employee.csv')
print(df_emp[df_emp['Employee Name'].str.startswith('J',na=False)])

