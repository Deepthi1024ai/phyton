import pandas as pd 
import numpy as np 
 
exam_data = { 
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 1, 1, 2, 1, 1, 2], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes'] 
} 
labels = ['a','b','c','d','e','f','g','h','i','j'] 
 
df = pd.DataFrame(exam_data, index=labels) 
print("DataFrame created from dictionary:") 
print(df) 
 
df.loc['d','name'] = 'Suresh' 
print("\nDataFrame after updating name 'James' to 'Suresh':") 
print(df) 
 
salaries = [50000, 60000, 75000, 45000, 55000, 80000, 70000, 48000, 62000, 78000] 
df['salary'] = salaries 
print("\nDataFrame after adding 'salary' column:") 
print(df) 
 
column_headers = df.columns.tolist() 
print("\nList of column headers:", column_headers)
