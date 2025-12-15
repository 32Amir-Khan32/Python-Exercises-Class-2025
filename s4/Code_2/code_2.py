i = 0
while i < 6:
    i += 1
    if i == 3:
        print(f"Skipping {i}")
        continue
    print(f"Processing: {i}")