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
print(dataFrame)
