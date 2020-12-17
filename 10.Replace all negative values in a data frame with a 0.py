import pandas as pd

data_dict = {'A':[1,-5,3,-7],
             'B':[-5,8,-7,2],
             'C':[5,-4,-4,2],
             'D':[-6,5,7,-4]}

df = pd.DataFrame(data_dict)
print(df)
df[df<0]=0
print(df)