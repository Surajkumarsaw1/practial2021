import pandas as pd 
data_dictionary = {'A':[91,52,23,74],
                   'B':[95,83,76,62],
                   'C':[65,46,94,27],
                   'D':[66,25,77,44]}
df = pd.DataFrame(data_dictionary)
ser = df.stack()
print(ser.nlargest(3))
"""
print(df.nlargest(3,['A'])['A'])
print(df.nlargest(3,['B'])['B'])
print(df.nlargest(3,['C'])['C'])
print(df.nlargest(3,['D'])['D'])

print(df.nsmallest(3,['A'])['A'])
print(df.nsmallest(3,['B'])['B'])
print(df.nsmallest(3,['C'])['C'])
print(df.nsmallest(3,['D'])['D'])
"""