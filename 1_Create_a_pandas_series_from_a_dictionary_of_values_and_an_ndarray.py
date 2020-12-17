import numpy as np
import pandas as pd

students = {"Aniket":78, "Aryan":73, "Suraj":90}
print("Dictionary is ",students)
series = pd.Series(students)
print("Series created form dictionary is :")
print(series)

#print(series["Aryan"])

arr = np.arange(4)
print("Array is ",arr)
series2 = pd.Series(arr, index=['A','B','C','D'])
print("Series created from array is :")
print(series2)
