import pandas as pd 
test = pd.Series([2,4,5,7,9,12,21])
percentile = test.quantile(.75)
print("75th Percentile is ",percentile)
print("Values in series greater than 75th percentile are :")
for x in range(len(test)):
    if test[x] > percentile:
        print(test[x])
        