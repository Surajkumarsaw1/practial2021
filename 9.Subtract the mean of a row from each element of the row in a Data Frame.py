import pandas as pd 
data_dict = {'A':[91,52,23,74],
             'B':[95,83,76,62],
             'C':[65,46,94,27],
             'D':[66,25,77,44]}
df = pd.DataFrame(data_dict)
row_mean = df.mean(axis=1)
print("Row mean are :\n",row_mean)
print("DataFrame after substracting row \
mean from each element of row :")
print(df.subtract(row_mean, axis = 0))
