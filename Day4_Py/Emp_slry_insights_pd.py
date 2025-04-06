import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)

#the average salary of employees in each department.
avg_salary = df.groupby('Department')['Salary'].mean().round(1).reset_index()
print("Average Salary of Dep:\n", avg_salary)

#the highest-paid employee in each department.
highest_paid = df.loc[df.groupby('Department')['Salary'].idxmax()].reset_index()
print("\nHighest paid employee in each dep:")
print(highest_paid[['Department','Employee','Salary']])

#how many employees have more than 5 years of experience and earn a salary above $65,000.

employees = df[(df['Experience']>5) & (df['Salary']>=65000)].reset_index()
print("\n",employees)

#a new column “Seniority”:
    #“Junior” (Experience < 5 years)
	#“Mid-Level” (Experience between 5-10 years)
	#“Senior” (Experience > 10 years)

df['Seniority'] = df['Experience'].apply(lambda exp:'Junior' if exp<5 else ('Mid level' if exp<=10 else 'Senior'))
print("\n", df[['Employee', 'Experience', 'Seniority']])

#Sort employees by salary in descending order, showing only “IT” department employees.

it_sorted = df[df['Department']=='IT'].sort_values(by='Salary', ascending=False)
print("\n",it_sorted[['Employee','Department', 'Salary']])