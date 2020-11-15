# importing pandas module.
import pandas as pd

# creating the dataframe named data.
data = pd.DataFrame({'Roll No.': ['123', '456', '789', '999'],
                     'Name': ['John', 'Jack', 'Andrew', 'Max'],
                     'Subject': ['Statistics', 'Statistics', 'Statistics', 'Statistics'],
                     'Marks': [98, 85, 89, 75]})

# creating column named index in the dataframe.
data['Index'] = data.index

# printing the dataframe named data.
print(data)