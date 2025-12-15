month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        result = "A weekday in April"
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        result = "A weekday in May"
    case _:
        result = "No match"

print(result)