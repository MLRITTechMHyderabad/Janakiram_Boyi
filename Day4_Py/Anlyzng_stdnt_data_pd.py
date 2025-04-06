import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)

#Find the average marks for each subject
avg_marks = df.groupby('Subject')['Marks'].mean().reset_index()
print(avg_marks)

#Identify students who scored above 85 and had less than 90% attendance
scored_85 = df[(df['Marks']>85) & (df['Attendance']<=90)].reset_index(drop = True)
print("\n",scored_85)

#Add a new column “Grade” based on marks:
	#90+ → “A”
	#80-89 → “B”
	#70-79 → “C”
	#< 70 → “D”
#df['Seniority'] = df['Experience'].apply(lambda exp:'Junior' if exp<5 else ('Mid level' if exp<=10 else 'Senior'))

df['Grade'] = df['Marks'].apply(lambda exp: 'A' if exp>=90 else ('B' if exp>=80 else('C' if exp>=70 else'D')))

print("\n",df[['Student','Subject','Grade','Marks']])

#Count how many students received each grade.

grade_count = df["Grade"].value_counts().reset_index()
print("\n",grade_count)

#Find out if attendance affects performance by calculating the correlation between marks and attendance.
correlation = df['Marks'].corr(df['Attendance'])
print("\nThe correlation between marks and attendance :",correlation)