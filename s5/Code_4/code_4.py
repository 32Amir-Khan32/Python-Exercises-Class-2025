def check_password_strength(password):
    strength_score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength_score += 2
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase
    if any(char.isupper() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter")
    
    # Check for lowercase
    if any(char.islower() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one number")
    
    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength_score += 1
    else:
        feedback.append("Add at least one special character")
    
    # Determine strength level
    if strength_score >= 5:
        strength_level = "Strong"
    elif strength_score >= 3:
        strength_level = "Medium"
    else:
        strength_level = "Weak"
    
    return strength_score, strength_level, feedback

def password_analyzer():
    password = input("Enter a password to check its strength: ")
    score, level, suggestions = check_password_strength(password)
    
    print(f"\nPassword Analysis for: {password}")
    print(f"Strength Score: {score}/5")
    print(f"Strength Level: {level}")
    
    if suggestions:
        print("\nSuggestions for improvement:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Great! Your password is strong.")

# Uncomment to test interactively
# password_analyzer()