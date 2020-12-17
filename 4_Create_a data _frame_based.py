import pandas as pd
data = dict()
data["Product Name"]=["Fan","Phone","Book","Watch"]
data["Cost"]=[4000,23000,500,12000]
data["Quantity"] = [2,1,8,4]
data_ecommerce = pd.DataFrame(data)
print(data_ecommerce)
print(data_ecommerce.describe())