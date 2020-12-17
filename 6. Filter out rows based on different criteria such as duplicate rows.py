import pandas as pd
students =[('Akash',20,'Mumbai'),
           ('Jay',17,'Delhi'),
           ('Akash',20,'Mumbai'),
           ('Satyam',30,'London'),
           ('Satyam',30,'London'),
           ('Satyam',30,'London'),
           ('Jay',17,'Delhi'),
           ('Rahul',20,'Mumbai')]
dfobj = pd.DataFrame(students, columns=['Name','Age','City'])
print(dfobj)
duplicateRowsDF = dfobj[dfobj.duplicated()]
print("Duplicate Rows are :")
print(duplicateRowsDF)
duplicateNames = dfobj[dfobj.duplicated(['Name'])]
print("Duplicate as per name :")
print(duplicateNames)
duplicateAgesCity = dfobj[dfobj.duplicated(['Age', 'City'])]
print("Deplicate as per Age and City :")
print(duplicateAgesCity)
