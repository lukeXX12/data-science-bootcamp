import pandas as pd
df = pd.read_csv("DataCleaning/messy_employees.csv")
print(df)
print(df.shape)
df.info()
print(df.dtypes)
print(df.duplicated().sum())
print(df.isna().sum())
## remove duplicate  employees
df = df.drop_duplicates()

#Age to numeric and drop missing values
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df =df.dropna(subset=["Age"])
df =df[df["Age"].between(18, 100)]
#Salary and department problems
df["Salary"] =df["Salary"].astype(str).str.replace(",", "", regex=False)
df["Salary"] = pd.to_numeric(df["Salary"], errors ="coerce")
df["Salary"]= df["Salary"].fillna(df["Salary"].median())
df["Salary"]=df["Salary"].round(0).astype(int)
df["Department"] =df["Department"].fillna('Unknown')
df['City'] = df['City'].str.title()
df["AnnualSalary"]=df['Salary']*12
def salary_category(salary):
    if salary <2500 :
         return "Low"
    elif salary <4000:
        return "Medium"
    else: 
        return "High"
df['SalaryCategory'] = df['Salary'].apply(salary_category)

summary = df.groupby("Department").agg(
    employee_count = ('Name','count'),
    average_salary = ('Salary', 'mean'),
    total_payroll =( 'Salary', 'sum')
)
summary['average_salary'] =summary['average_salary'].round(0).astype(int)

#Final Check
print(df.isna().sum())
print(df.duplicated().sum())
print(df.dtypes)
print(df)
print(summary)
df.to_csv("DataCleaning/cleaned_employees.csv",
          index =False
          )
summary.to_csv(
    "DataCleaning/dep_summary.csv"
)


