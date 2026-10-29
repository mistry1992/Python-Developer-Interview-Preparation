data = [
    {"name": "Rahul","Age": 25},
    {"name": "Priya","Age": 22},
    {"name": "Amit","Age": 28},
        ]
sorted_data = sorted(data, key=lambda x:x["Age"])
print(sorted_data)