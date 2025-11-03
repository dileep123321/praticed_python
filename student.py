students = {"Dileep": 89, "Bhara": 76, "Chethan": 92, "Yogesh": 88}
topper = max(students, key=students.get)
print("All Marks:", students)
print(f"Topper: {topper} - {students[topper]}")
