students = [
    ("Ali", ["Fizika", "Matematika"]),
    ("Laylo", ["Ingliz tili"]),
    ("Jasur", ["Matematika", "Informatika"])
]

fan = input()

amount = 0

for student in students:
    if fan in student[1]:  
        amount += 1

print(amount)
