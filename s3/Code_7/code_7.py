original = {
    "name": "AmirKhan",
    "age": 25
}

copy1 = original.copy()
copy2 = dict(original)

copy1["city"] = "Tehran"

print(f"اصل: {original}")
print(f"کپی 1: {copy1}")
print(f"کپی 2: {copy2}")