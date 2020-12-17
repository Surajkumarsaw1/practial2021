import pandas as pd 
exam_data = [(1234,"Ankit",460,92.0,"A+"),
             (1235,"Payal",400,80.0,"A"),
             (1236,"Charu",385,77.0,"B"),
             (1237,"Aryan",462,92.4,"A+"),
             (1238,"Kajal",280,56.0,"C")]
exam_result = pd.DataFrame(exam_data,
                          columns=["Admno","Name","Total","Percentage","Grade"],
                          index = ["A","B","C","D","E"])
print(exam_result)

print("Columns Labels are")
print(exam_result.columns)
print("Row Labels are")
print(exam_result.index.values)
print("Data Type of Columns are ")
print(exam_result.dtypes)
print("Dimentions of DataFrame are ")
print(exam_result.shape)
