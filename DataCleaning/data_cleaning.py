import pandas as pd
df = pd.read_csv("DataCleaning/messy_employees.csv")

#print(df)
# investigation of the DataFrame

#print(df.info)

#print(df.describe(include="all"))

#missing values in each column
# print(df.isnull().sum())

# how many duplicate rows

# print(df.duplicated().sum())

#dataTypes of columns
# print(df.dtypes)

#missing values
# print(df.isna())
# print(df.isna().sum())

#Handling missing values
#Remove rows
# clean_df =df.dropna()
# print(clean_df)

#Replacing missing values with average salary
#df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

#for categorical column
# df["Department"] = df["Department"].fillna("Unknown")

# print(df[df.duplicated()])
# df = df.drop_duplicates()
# print(df.duplicated().sum())


#AGE problems
#print(df[df["Age"] <= 0])
import numpy as np
df["Age"] = pd.to_numeric(df["Age"], errors= "coerce")
print(df[df["Age"] <= 0])

#remove rows where age  is missing
df= df.dropna(subset =["Age"])
print(df)

# Salary problem
print(df["Salary"].dtype)
df["Salary"] =df["Salary"].astype(str).replace(",", "")
df["Salary"] = pd.to_numeric(df["Salary"], errors ="coerce")
print(df["Salary"].dtype)
print(df)

#Clean the city names
df["City"] = df["City"].str.title()
print (df["City"].unique())

#Missing department
df["Department"] = df["Department"].fillna("Unknown")
print(df["Department"].unique())

# inspect cleaned DataFrame
print(df)
print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())


#Annual salary
df["AnnualSalary"] = df["Salary"] * 12


#Classify employees
def salary_category(salary):
    if salary <2500:
        return "Low"
    elif salary <4000:
        return "Medium"
    else: 
        return "High"

    
df["SalaryCategory"] =df["Salary"].apply(salary_category)

print(df[["Name" , "Salary", "SalaryCategory"]])
df[df["Age"] <= 0].drop()