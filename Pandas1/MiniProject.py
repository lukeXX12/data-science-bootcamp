import pandas as pd
df = pd.read_csv("Pandas1/employees.csv")
#print Number of employees, average salary,Highest-lowesd salary

print( "Number of employees: ",len(df),
      "\n average Salary is: ", df["Salary"].mean(), 
      "\n Max Salary is :" ,df["Salary"].max(),
       "\n Min Salary is:" , df["Salary"].min())
#Print all IT employees
print(df[df["Department"] =="IT"])
#print everyone earning over 3000
print(df[df["Salary"] > 3000])
#add NewSalary column with 10% raise
df["NewSalary"]  = (df["Salary"] * 1.1).astype(int)

df.to_csv("Pandas1/employees.csv", index=False)