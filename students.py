import csv

# WRITE TO FILE #
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# READ FROM FILE #
# students = []
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append(row)
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
