students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]


highest_avg = 0
top_student = ""

for name,scores in students:
    avg = sum(scores)/len(scores)
    
    if name == "Bob":
        print("Average grade of Bob :")
        print(avg)
        
    if avg>highest_avg:
        highest_avg = avg
        top_student = name 
    

    count = 0
    if avg >50:
        count+=1
        
        
print("Student with the highest average grade:", top_student)
print("Number of students who passed:", count)