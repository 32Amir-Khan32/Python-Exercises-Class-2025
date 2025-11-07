# اطلاعات دانشجو
amir_info = {
    "personal": {
        "name": "AmirKhan",
        "age": 25,
        "city": "Tehran"
    },
    "academic": {
        "major": "Computer Science",
        "gpa": 18.5,
        "courses": ["Python", "Algorithms", "Database"]
    },
    "contact": {
        "email": "amir.khan@university.com",
        "phone": "+98-912-345-6789"
    }
}

# نمایش اطلاعات
print("=== اطلاعات AmirKhan ===")
for section, details in amir_info.items():
    print(f"\n{section.upper()}:")
    for key, value in details.items():
        print(f"  {key}: {value}")