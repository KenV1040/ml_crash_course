# Note: All of this is me following along the code lab.
from __future__ import print_function

import pandas as pd 

# Prints out panda version
print(pd.__version__)

# Create a series by using the Series object
sample = pd.Series(['sample data', 'sampeldata2'])
data = pd.Series([2300, 23000])

# To create a DataFrame, pass a dict mapping.
dataFrame = pd.DataFrame({'sample':sample, 'data':data})
#print(dataFrame)
# If the two series don't match in length, the missing values are filled with NA/NaN values

# To load an entire file into a DataFrame:
california_housing_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
#print(california_housing_df.describe())

# Prints the first few records of DataFrame
print(california_housing_df.head)