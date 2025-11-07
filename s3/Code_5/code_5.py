myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    }
}

for parent_key, child_dict in myfamily.items():
    print(f"{parent_key}:")
    for key, value in child_dict.items():
        print(f"  {key}: {value}")