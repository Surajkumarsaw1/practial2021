import pandas as pd 
quarterly_sales={"Items Category":
["Cold Drink","Chips","Chocolate","Chips","Cold Drink"],
"Items Name":
["Coke","Lays","Dairy Milk","Kurkure","Fanta"],
"Expenditure":
[35,20,40,20,65]}

df_sales = pd.DataFrame(quarterly_sales)
#print(df_sales)
print(df_sales.groupby("Items Category")["Expenditure"].sum
())
