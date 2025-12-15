user_role = "editor"

match user_role:
    case "admin" | "superuser":
        access_level = "Full Access"
    case "editor":
        access_level = "Edit Access"
    case "viewer":
        access_level = "Read Only"
    case _:
        access_level = "No Access"

print(f"Role: {user_role}")
print(f"Access Level: {access_level}")