import pandas as pd
df_emp=pd.read_csv('employee.csv')
print(df_emp[(df_emp['Department']=='Marketing') & (df_emp['SALARY']<60000)])



