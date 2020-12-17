import numpy as np
import pandas as pd

data_dict = {"A":[10,40,np.NaN],
            "B":[20,np.NaN,50],
            "C":[np.NaN,60,70]
            }
df = pd.DataFrame(data_dict)
print(df)
df.fillna(999,inplace=True)
print(df)

#df1 = df.fillna(999)
#print(df1)
#df2 = df.replace(np.NaN,999)
#print(df2)