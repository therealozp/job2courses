import pandas as pd

df = pd.read_csv('course-inventory.csv')
print(df.head(5))

for rows in df.iterrrows(): 
    # process data
    # insert into table
    