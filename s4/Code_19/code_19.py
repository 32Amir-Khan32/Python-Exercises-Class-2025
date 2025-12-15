search_list = [10, 20, 30, 40, 50]
search_value = 35

for num in search_list:
    if num == search_value:
        print(f"Found {search_value}")
        break
else:
    print(f"{search_value} not found in the list")