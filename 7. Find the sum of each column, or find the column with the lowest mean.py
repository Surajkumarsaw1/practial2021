import numpy as np
import pandas as pd
x = [(11,12,13,14,15),
     (91,12,73,34,55),
     (16,17,18,19,20),
     (61,71,81,91,101)]

df = pd.DataFrame(x,
columns = ["A","B","C","D","E"],
index = ["a","b","c","d"])

print('DataFrame :')
print(df)
print('Sum of columns :')
print(df.sum(axis = 0))
print('Minimum mean column')
var = ((df.mean(axis = 0)).sort_values(ascending
=True)[0:1])
print(var)
