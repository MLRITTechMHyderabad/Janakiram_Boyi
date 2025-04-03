students = [
    "Alice", [85,90,78,92],
    "Bob", [60,65,70,75],
    "Charlie", [40,45,50,55],
    "David", [95,100,98,92]
] 


print( 'Dictionary of students and their grades : \n ', students , "\n")

#Average of 
def calculate_avg(grades):
    return sum(grades)/len(grades)

print('Average grade for Alice: ', calculate_avg(students['Alice']), '\n')

#Highest avg Grade
high_avg_student = ""
high_avg = 0

for student, grades in students.items():
    avg = calculate_avg(grades)
    if avg>high_avg:
        high_avg =avg
        high_avg_student = student

print("Student with the highestv average grade: \n", high_avg_student, "with avg grade ", high_avg )
