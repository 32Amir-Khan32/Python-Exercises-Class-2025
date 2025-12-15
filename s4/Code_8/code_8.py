day_number = 4

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"
    case 5:
        day_name = "Friday"
    case 6:
        day_name = "Saturday"
    case 7:
        day_name = "Sunday"
    case _:
        day_name = "Invalid day"

print(f"Day {day_number} is {day_name}")