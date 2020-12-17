import pandas as pd
train = {"Train No.":[17738,21883,17548,23173],
         "Speed":[92,108,24,67],
         "City":['Delhi','Punjab','Goa','Assam']
         }
df_train = pd.DataFrame(train)

# Exporting df_train as trian.csv file in same directory as of code.
df_train.to_csv('trains.csv', index=False)

# Importing train.csv from same directory as of code.
train_csv = pd.read_csv('trains.csv')
print(train_csv)