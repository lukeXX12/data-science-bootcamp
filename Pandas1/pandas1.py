#printing the version of pandas

# import pandas as pd
# print(pd.__version__)

#usinng pandas to create a data frame

# import pandas as pd
# data ={
#     "Name":["Ana", "Luka", "Nino"],
#     "Age":[20, 21, 19],
#     "Salary":[1000, 2000, 1500]

# }
# df =pd.DataFrame(data)
# print(df)

#Reading data from a CSV file with pandas
import pandas as pd
df =pd.read_csv("Pandas1/employees.csv")
#print (df)

#first 5 rows of the data frame
#print (df.head())

#last 5 rows of the data frame
#print (df.tail())

#print the column names of the data frame
#print(df.columns)

#print the info of the data frame
#print(df.info())

#print(df.describe())


#exrcise1
#How many employees are there in the data frame?
#df = pd.read_csv("Pandas1/employees.csv")
#print("number of employees in the dataframe: ", len(df))

#what columns are present in the data frame?
#print("columns present in the data frame: ", df.columns)

#whar is the average salary of the employees?
#print("average salary of the employees: ", df["Salary"].mean())

##Data selection and filtering in pandas
##selecting a single column
#df = pd.read_csv("Pandas1/employees.csv")
#print(df["Name"])
#print(df["Salary"])

##multiple columns selection
#print(df[["Name", "Salary"]])

#single row
#print(df.iloc[0])

#rows (2-4)
#print(df.iloc[2:4])


##filtering data 

##employees with salary greater than 2000
# print(df[df["Salary"] > 2000])

##employees from the IT department
# print(df[df["Department"] == "IT"])

##IT employees earning over 3000
# print(
#     df[
#         (df["Department"] == "IT" )&
#           (df["Salary"] > 3000)
#     ]
# )

##Exercise 2
##Employees younger than 25
# print("employees younger than 25", df[df["Age"] <25])
#employees from finance department
# print("employees from finance department", df[df["Department"]== "Finance"])
#employees with salary greater than 3000
#print("salaries below 3000",df[df["Salary"] < 3000])


#Sorting data in pandas
# print("data frame sorted by salary in ascending order", df.sort_values("Salary"))

# #Sorting data in descending order
# print(df.sort_values("Salary" , ascending=False))
# #New Columns in pandas

# df["Raise"] = df["Salary"] * 0.1
# print("data frame with new column raise", df)

# df.loc[2,"Salary"] = None
# print("data frame with missing value", df)
# print(df.isnull().sum())
# clean = df.dropna()
# print("data frame after dropping missing values", clean)
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print("data frame after filling missing values with mean", df)



# import pandas as pd
# df = pd.read_csv("Pandas1/employees.csv")
# #print Number of employees, average salary,Highest-lowesd salary

# print( "Number of employees: ",len(df),
#       "\n average Salary is: ", df["Salary"].mean(), 
#       "\n Max Salary is :" ,df["Salary"].max(),
#        "\n Min Salary is:" , df["Salary"].min())
# #Print all IT employees
# print(df[df["Department"] =="IT"])
# #print everyone earning over 3000
# print(df[df["Salary"] > 3000])
# #add NewSalary column with 10% raise
# df["NewSalary"]  = (df["Salary"] * 1.1).astype(int)

# df.to_csv("Pandas1/employees_updated.csv", index=False)


# AverageIT = df[df["Department"] == "IT"]["Salary"].mean()
# print(AverageIT)

# averageHR = df[df["Department"] == "HR"]["Salary"].mean()
# print(averageHR)

# averageFinance = df[df["Department"] == "Finance"]["Salary"].mean()
# print(averageFinance)

# maxavg = max(AverageIT, averageHR, averageFinance)
# print(maxavg)
# #Stupid way of doing easy job



# # this is easier


# avg_salaries = df.groupby("Department")["Salary"].mean()
# max_dept = avg_salaries.idxmax()
# max_avgsalary = avg_salaries.max()
# print(f"Department With max avg Salary: {max_dept}(${max_avgsalary:,.2f})")


# #sorted 
# rankedDepartments = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)

# print(rankedDepartments)

# total_payroll_by_Dep = df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
# print(total_payroll_by_Dep)
# import numpy as np
# df =pd.DataFrame(
#     [[1,2,3 ],[4,5,6],[7,8,9], [np.nan, np.nan, np.nan]],
#     columns=["A","B","C"]
# )

# print(df.agg(["sum", "min"]))


#Bonus task for .agg

print(df.groupby("Department")["Salary"].agg(["mean", "count"]))