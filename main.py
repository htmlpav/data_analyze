import csv

def calculate_average(data, subject):
    average = 0
    sum = 0
    for mark in data:
        sum += int(mark[subject])
    return sum / len(data)
def best_student(data, common_keys):
    print("\nBest student:")
    marks = []
    sum = 0
    max = 0
    nom = 0
    for i in range(len(data)):
        for subject in common_keys:
            sum += int(data[i][subject])
        # print(sum)
        if max < sum:
            max = sum
            nom = i
        sum = 0
    print(data[nom]["name"], max)
def average_mark_on_each_subject(data, common_keys):
    print("\nAverage mark on each subject:")
    for subject in common_keys:
        print(subject, calculate_average(data, subject=subject))
def students_count(data):
    print("Кол-во студентов:")
    print(len(data))
with open("students.csv", "r", encoding="utf-8") as file:
    students = csv.DictReader(file)
    data = list(students)

    # for line in data:
    #     print(line)
common_keys = list(data[0].keys())
del common_keys[0]
students_count(data)
average_mark_on_each_subject(data, common_keys)
best_student(data, common_keys)


