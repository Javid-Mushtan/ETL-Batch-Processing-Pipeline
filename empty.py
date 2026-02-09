import pandas as pd
# this will use only for checking the gnerated csv file have any null values or errors
df = pd.read_csv('employee_data.csv')
print(df)