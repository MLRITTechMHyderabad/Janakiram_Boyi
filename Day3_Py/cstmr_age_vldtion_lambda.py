customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

eligible_customers = filter(lambda c: 18<=c["age"]<=40, customers)

discounted_customers = map(
    lambda c:{
        "name": c["name"],
        "age": c["age"],
        "total_purchase": round(
            c["total_purchase"]*90 if 18<=c["age"]<=25 
            else c["total_purchase"]*0.95, 2
        )
    }, eligible_customers
)

result = list(discounted_customers)
print(result)

    