employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

print(employees, "\n")

adjusted_employees = list(
    map(
        lambda emp : {
            "name" : emp["name"],
            "salary" : round (
                emp["salary"]*( 
                1.10 if emp["rating"] in [4,5] else
                1.05 if emp["rating"] == 3 else
                0.97 
            ),2
            ), 
            "rating" : emp["rating"]
        }, employees
    )
)
print()
print(adjusted_employees)