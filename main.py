import csv

with open("students.csv", "r", encoding="utf-8") as file:
    students = csv.DictReader(file)
    data = list(students)

    # for line in data:
    #     print(line)
print(data[0]["math"]) # 100