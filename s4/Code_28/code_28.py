correct_password = "AmirKhan@2024"
attempts = 3

while attempts > 0:
    password = input(f"Enter password ({attempts} attempts left): ")
    
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access Denied! No attempts left.")
        else:
            print("Incorrect password. Try again.")